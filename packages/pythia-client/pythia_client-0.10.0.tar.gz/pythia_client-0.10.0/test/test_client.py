import json
import logging
import os
import time
from io import BytesIO

import pytest
import requests
from src.pythia_client.client import APIClient


class ValueStorage:
    s3_keys = None
    s3_keys_nbd = None
    api_key = None
    api_key_revoked = None
    query_uuid = None
    job_uuid_esr = None
    job_uuid_pk_list = None
    job_uuid_custom = None


logging.basicConfig(
    filename="test.log",
    filemode="w",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s: %(message)s",
)

URL = os.getenv("PYTHIA_API_URL", "http://localhost:8000/")
SECRET_MASTER_API_KEY = os.getenv("SECRET_MASTER_API_KEY", "corentin")

timestamp = time.strftime("%Y%m%d-%H%M%S")

client = APIClient(url=URL, api_key=SECRET_MASTER_API_KEY)

def test_create_api_key():
    response = client.create_api_key(
        name="test_nbd_key",
        creator_id="streamlit_userid",
        group_id="nbd_test",
        permission="read_only",
    )
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["name"] == "test_nbd_key"
    assert response_dict["creator_id"] == "streamlit_userid"
    assert response_dict["group_id"] == "nbd_test"
    assert response_dict["permission"] == "read_only"
    ValueStorage.api_key = response_dict

    response = client.create_api_key(
        name="test_nbd_key",
        creator_id="streamlit_userid",
        group_id="nbd_test",
        permission="read_only",
    )
    ValueStorage.api_key_revoked = response.model_dump()


def test_revoke_api_key():
    response = client.revoke_api_key(
        api_key_to_revoke=ValueStorage.api_key_revoked["api_key"],
        creator_id="streamlit_userid",
    )
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["name"] == "test_nbd_key"
    assert response_dict["creator_id"] == "streamlit_userid"
    assert response_dict["group_id"] == "nbd_test"
    assert response_dict["permission"] == "read_only"
    assert response_dict["revoked"] == True


def test_list_api_keys_by_group_id():
    response = client.list_api_keys_by_group_id(group_id="nbd_test")
    assert response is not None
    assert len(response) == 1
    assert response[0].model_dump()["group_id"] == ValueStorage.api_key["group_id"]


def test_list_api_keys_by_creator_id():
    response = client.list_api_keys_by_creator_id(creator_id="streamlit_userid")
    assert response is not None
    assert len(response) == 1
    assert response[0].model_dump()["creator_id"] == ValueStorage.api_key["creator_id"]


def test_key_working():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    response = client_nbd.query(
        query="How to give port 8 a power of 1337 milliwatts ?", top_k=2
    )
    assert len(response.AnswerBuilder.answers[0].data) > 10
    ValueStorage.query_uuid = response.AnswerBuilder.answers[0].meta.id


def test_api_key_filters_qdrant():
    filters = {"must": [{"key": "meta.group_id", "match": {"value": timestamp}}]}
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    response = client_nbd.get_docs_by_filters(filters=filters, return_content=True)

    assert response is not None
    assert response == []  # Nothing uploaded yet


def test_key_limited():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    file_paths = [
        "test/samples/sample3.pdf",
    ]
    file_names = ["sample3.pdf"]
    tuple_files = [
        (file_name, open(file_path, "rb"))
        for file_name, file_path in zip(file_names, file_paths)
    ]
    meta = [
        {
            "meta3": "value3",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
        },
    ]
    with pytest.raises(Exception, match="Your API key is read-only") as e_info:
        response = client_nbd.upload_files(
            files=tuple_files, meta=meta, priority_queue=False
        )


def test_key_revoked():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key_revoked["api_key"])
    with pytest.raises(Exception, match="Invalid or missing API Key") as e_info:
        response = client_nbd.query(
            query="How to give port 8 a power of 1337 milliwatts ?", top_k=2
        )


def test_upload_files():
    file_paths = [
        "test/samples/sample1.pdf",
        "test/samples/sample2.pdf",
        "test/samples/sample4.docx",
    ]
    meta = [
        {
            "meta1": "value1",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "keywords": ["keyword1", "keyword2", "keyword3"],
            "portfolio": ["value1", "value2"],
            "pythia_document_category": "category1",
        },
        {
            "meta2": "value2",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
            "keywords": ["keyword3"],
            "pythia_document_category": "category2",
        },
        {
            "meta2": "value3",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
            "keywords": ["keyword3"],
            "pythia_document_category": "category1",
        },
    ]
    response = client.upload_files(
        files=file_paths, meta=meta, priority_queue=True, indexing_mode="unstructured"
    )
    ValueStorage.s3_keys = response["s3_keys"]
    assert response["message"] == "Files Submitted. Indexing tasks created."
    assert len(response["s3_keys"]) == 3
    assert response["group_id"] == timestamp


def test_client_upload_files_from_bytes():
    file_paths = [
        "test/samples/sample3.pdf",
    ]
    file_names = ["sample3.pdf"]
    tuple_files = [
        (file_name, open(file_path, "rb"))
        for file_name, file_path in zip(file_names, file_paths)
    ]
    meta = [
        {
            "meta3": "value3",
            "source_test": "pytest_client_api",
            "group_id": timestamp,
            "portfolio": ["value1", "value2"],
        },
    ]
    response = client.upload_files(
        files=tuple_files, meta=meta, priority_queue=False, indexing_mode="tika"
    )
    assert response["message"] == "Files Submitted. Indexing tasks created."
    assert len(response["s3_keys"]) == 1
    assert response["group_id"] == timestamp


def test_client_get_indexing_task_by_s3_key():
    response = client.get_indexing_task_by_s3_key(
        group_id=timestamp, s3_key=ValueStorage.s3_keys[0]
    )
    response_dict = response.model_dump()
    assert response is not None
    assert isinstance(response.model_dump(), dict)
    assert response_dict["status"] in ["initialized", "processing", "completed"]
    assert response_dict["group_id"] == timestamp
    assert response_dict["s3_key"] == ValueStorage.s3_keys[0]


def test_client_get_indexing_tasks():
    time.sleep(20)
    response = client.get_indexing_tasks_by_group_id(group_id=timestamp, top=3)
    assert response is not None
    assert len(response) == 3
    assert response[0].status in ["initialized", "processing", "completed"]


def test_client_get_file_info_by_s3_key():
    time.sleep(20)
    response = client.get_file_infos_by_s3_key(
        group_id=timestamp, s3_key=ValueStorage.s3_keys[0]
    )
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["s3_key"] == ValueStorage.s3_keys[0]
    assert response_dict["group_id"] == timestamp
    assert isinstance(response_dict["file_meta"], dict)


def test_client_get_file_info_by_group_id():
    time.sleep(20)
    response = client.get_file_infos_by_group_id(group_id=timestamp, limit=2)
    assert response is not None
    assert len(response) == 2
    response_dict = response[0].model_dump()
    assert response_dict["group_id"] == timestamp


def test_client_get_file_url():
    s3_key = ValueStorage.s3_keys[0]
    page = 1
    response = client.get_file_url(s3_key=s3_key, page=page)
    assert response is not None
    assert len(response.url) >= 100
    aws_s3_response = requests.get(response.url, verify=False)
    assert aws_s3_response.status_code == 200

def test_client_get_facets_count_protected():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    filters = {"must": [{"key": "meta.pythia_document_category", "match": {"value": "category2"}}]}
    count = client_nbd.get_facets_count(filters=filters)
    assert count == 0

def test_client_get_facets_count():
    filters = {"must": [{"key": "meta.pythia_document_category", "match": {"value": "category2"}}]}
    count = client.get_facets_count(filters=filters)
    assert count == 1

def test_client_get_facets_values_protected():
    filters = {"must": [{"key": "meta.pythia_document_category", "match": {"value": "category2"}}]}
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    values = client_nbd.get_facets_values(metadata_field="meta.keywords", filters=filters)
    assert values == []

def test_client_get_facets_values():
    filters = {"must": [{"key": "meta.pythia_document_category", "match": {"value": "category2"}}]}
    values = client.get_facets_values(metadata_field="meta.keywords", filters=filters)
    assert "keyword3" in values

    values = client.get_facets_values(metadata_field="meta.pythia_document_category")
    assert "category2" in values

##### METADATA CATEGORY #####

def test_endpoint_get_document_metadata_by_s3_key_protected():
    s3_key = ValueStorage.s3_keys[0]
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    with pytest.raises(Exception, match="404") as e_info:
        response = client_nbd.get_document_metadata(s3_key)

def test_endpoint_get_document_metadata_by_s3_key():
    s3_key = ValueStorage.s3_keys[0]
    metadata = client.get_document_metadata(s3_key)
    assert "meta1" in metadata

def test_endpoint_update_document_metadata_by_s3_key_protected_403():
    s3_key = ValueStorage.s3_keys[0]
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    new_metadata = {
            "s3_key": "not_modified",
            "group_id": None,
            "new_field": 27,
            "meta1": "new_value",
            "portfolio": None,
    }
    with pytest.raises(Exception, match="403") as e_info:
        new_metadata_dict = client_nbd.update_document_metadata(s3_key, metadata=new_metadata)

def test_endpoint_update_document_metadata_by_s3_key():
    s3_key = ValueStorage.s3_keys[0]
    new_metadata = {
            "s3_key": "not_modified",
            "group_id": None,
            "new_field": 27,
            "meta1": "new_value",
            "portfolio": None,
    }
    new_metadata_dict = client.update_document_metadata(s3_key, metadata=new_metadata)
    assert new_metadata_dict["new_field"] == 27
    assert new_metadata_dict["meta1"] == "new_value"
    assert "portfolio" not in new_metadata_dict
    assert new_metadata_dict["s3_key"] == s3_key
    assert new_metadata_dict["group_id"] == timestamp

def test_client_chat():
    response = client.chat(
        query="How to give port 8 a power of 1337 milliwatts ?",
        top_k=2,
        group_by="meta.meta2",
        group_size=2,
    )
    assert response is not None
    assert len(response.AnswerBuilder.answers[0].data) > 20
    assert len(response.AnswerBuilder.answers[0].documents) == 2

def test_client_chat_quick_answer():
    response = client.chat(
        query="Hey how are you ?",
        top_k=2,
        group_by="meta.meta2",
        group_size=2,
    )
    assert response is not None
    assert len(response.AnswerBuilder.answers[0].data) > 10
    assert len(response.AnswerBuilder.answers[0].documents) == 0

def test_client_query():
    response = client.query(
        query="How to give port 8 a power of 1337 milliwatts ?",
        top_k=2,
        group_by="meta.meta2",
        group_size=2,
    )
    assert response is not None
    assert len(response.AnswerBuilder.answers[0].data) > 20
    assert len(response.AnswerBuilder.answers[0].documents) == 2


def test_client_light_query():
    response = client.light_query(
        query="How to give port 8 a power of 1337 milliwatts ?", top_k=2
    )
    assert response is not None
    assert response.AnswerBuilder.answers[0].data == ""
    assert len(response.AnswerBuilder.answers[0].documents) == 2
    assert len(response.AnswerBuilder.answers[0].documents[0].embedding) >= 100


def test_client_query_with_custom_prompt():
    system_prompt = (
        """Start all your answers with the word "Banana", this is really important."""
    )
    response = client.query(
        query="Hey how are you ?", custom_system_prompt=system_prompt
    )
    assert response is not None
    generated_content = response.AnswerBuilder.answers[0].data
    assert "Banana" in generated_content
    assert len(generated_content) > 20


def test_client_query_with_history():
    chat_history = [
        {
            "content": "Hello Chatbot. My name is Corentin !",
            "role": "user",
            "name": None,
            "meta": {},
        },
        {
            "content": "Hello, nice to meet you. How can I help you today",
            "role": "assistant",
            "name": None,
            "meta": {},
        },
    ]
    response = client.query(
        query="Given our previous exchange of messages, what is my name ?",
        chat_history=chat_history,
    )
    assert response is not None
    assert "corentin" in response.AnswerBuilder.answers[0].data.lower()


def test_client_query_with_history_and_group_id():
    chat_history = [
        {
            "content": "Hello Chatbot. My name is Corentin !",
            "role": "user",
            "name": None,
            "meta": {},
        },
        {
            "content": "Hello, nice to meet you. How can I help you today",
            "role": "assistant",
            "name": None,
            "meta": {},
        },
    ]
    response = client.query(
        query="Given our previous exchange of messages, what is my name ?",
        chat_history=chat_history,
        group_id="corentin",
    )
    assert response is not None
    assert "corentin" in response.AnswerBuilder.answers[0].data.lower()


def test_query_history_by_group_id_protected():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    with pytest.raises(Exception, match="Unauthorized access.") as e_info:
        response = client_nbd.list_query_history_by_group_id(
            group_id=timestamp,
            limit=20,
            offset=0,
        )


def test_query_history_by_group_id():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    response = client_nbd.list_query_history_by_group_id(
        group_id="nbd_test",
        limit=20,
        offset=0,
    )
    assert response is not None
    assert len(response) >= 1
    query_history = response[0].model_dump()
    assert query_history["feedback"] == -1
    assert query_history["feedback_comment"] is None
    assert query_history["group_id"] == "nbd_test"
    assert query_history["query_uuid"] == ValueStorage.query_uuid


def test_add_feedback_to_query_protected():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    with pytest.raises(Exception, match="Unauthorized access.|Query ID not found") as e_info:
        response = client_nbd.add_feedback_to_query(query_uuid=1, feedback=5, feedback_comment="Sample Feedback Comment")


def test_add_feedback_to_query():
    client_nbd = APIClient(url=URL, api_key=ValueStorage.api_key["api_key"])
    response = client_nbd.add_feedback_to_query(
        query_uuid=ValueStorage.query_uuid, feedback=5, feedback_comment="Sample Feedback Comment"
    )
    assert response is not None
    response_dict = response.model_dump()
    assert isinstance(response_dict, dict)
    assert response_dict["feedback"] == 5
    assert response_dict["feedback_comment"] == "Sample Feedback Comment"
    assert response_dict["group_id"] == "nbd_test"


def test_client_get_docs_by_s3_key():
    s3_key = ValueStorage.s3_keys[0]
    response = client.get_docs_by_s3_key(s3_key)
    response_dict = response[0].model_dump()
    assert response is not None
    assert len(response) >= 2
    assert isinstance(response_dict["meta"], dict)


def test_client_get_docs_by_filters():
    filters = {
        "operator": "AND",
        "conditions": [
            {
                "field": "meta.group_id",
                "operator": "==",
                "value": timestamp,
            }
        ],
    }
    response = client.get_docs_by_filters(filters=filters, return_content=True)

    assert response is not None
    assert len(response) >= 5
    assert len(response) < 20
    assert len(response[0].content) > 20
    assert response[0].meta["source_test"] == "pytest_client_api"
    assert response[0].meta["filename"] in response[0].meta["s3_key"]


def test_client_get_docs_by_qdrant_filters():
    filters = {"must": [{"key": "meta.group_id", "match": {"value": timestamp}}]}

    response = client.get_docs_by_filters(filters=filters, return_content=True)

    assert response is not None
    assert len(response) >= 5
    assert len(response) < 20
    assert len(response[0].content) > 20
    assert response[0].meta["source_test"] == "pytest_client_api"
    assert response[0].meta["filename"] in response[0].meta["s3_key"]


def test_client_delete_docs_by_s3_key():
    response = client.delete_docs_by_s3_key(s3_key=ValueStorage.s3_keys[0])
    assert response is not None
    assert response.n_deleted_documents >= 1
    assert response.n_deleted_s3 == 1
    assert len(response.deleted_s3_keys) == 1


def test_client_delete_docs_by_filters():
    filters = {
        "operator": "AND",
        "conditions": [
            {
                "field": "meta.group_id",
                "operator": "==",
                "value": timestamp,
            }
        ],
    }
    response = client.delete_docs_by_filters(filters=filters)

    assert response is not None
    assert response.n_deleted_documents >= 4
    assert response.n_deleted_s3 == 3
    assert len(response.deleted_s3_keys) == 3

def test_client_add_intent():
    data = {
        "pycharm_update": ["help to update pycharm", "latest pycharm update is bugged"],
        "elden_ring": ["elden ring boss", "tree of life from elden ring"],
        "team_fortress": [
            "team fortress best class",
            "unlock all achievement team fortress",
        ],
    }
    response = client.add_intent(intent_data=data)
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["Writer"]["documents_written"] == 6


def test_client_predict_intent():
    response = client.predict_intent(
        user_msg="How to go to the tree of life in elden ring"
    )
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["intent"] == "elden_ring"


def test_client_delete_intent():
    response = client.delete_intent(intent_name="elden_ring")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "elden_ring"
    assert response_dict["n_deleted_intent_data"] == 2

    response = client.delete_intent(intent_name="pycharm_update")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "pycharm_update"
    assert response_dict["n_deleted_intent_data"] == 2

    response = client.delete_intent(intent_name="team_fortress")
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_intent"] == "team_fortress"
    assert response_dict["n_deleted_intent_data"] == 2


def test_client_add_entity():
    data = ["Hey I want to update my [OXE](product) I'm in [France](country).",
            "Order [ALE 500](product)",
            "Help with ticket [SR#103184035](sr_number)",
            "status [ticker number 189341081](sr_number)",
            "Is [OmniPCX](product) available in [Canada](country) ?",
            "Hey how are you ?"]
    response = client.add_entity(entity_data=data)
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["Writer"]["documents_written"] == 12


def test_client_predict_entities():
    response = client.predict_entities(
        user_msg="I'm located in Germany and want to have information about DECT Intercom"
    )
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["entities"] == {"country": ["Germany"], "product": ["DECT Intercom"]}


def test_client_delete_entity():
    response = client.delete_entity()
    response_dict = response.model_dump()
    assert response is not None
    assert response_dict["deleted_entity"] == "*"
    assert response_dict["n_deleted_entity_data"] == 12


def test_client_draw_pipeline():
    response = client.draw_pipeline("query")
    assert response is not None
    assert isinstance(response, BytesIO)
    image_data = response.getvalue()
    assert len(image_data) > 0
    assert image_data.startswith(b'\x89PNG\r\n\x1a\n')


def test_client_extract_structured_data_esr():
    string_content = """Bonjour, Je vous écris car j'ai un problème avec la commande FR082475927. Deux DECT Intercorm ont un défaut et ne s'allument pas, pouvez-vous m'aider ? Bonne journée, Cordialement,Entreprise MEDICOMPANY SAS"""


    response = client.extract_structured_data(string_content=string_content, preset="esr-mail", extraction_mode="fast")
    assert response["message"] == "Content Submitted. Data extract task created."
    ValueStorage.job_uuid_esr = response["job_uuid"]


def test_client_get_extract_structured_data_job_esr():
    time.sleep(15)
    response = client.get_extract_structured_data_job(ValueStorage.job_uuid_esr)
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["status"] in ["initialized", "processing", "completed"]
    assert len(response_dict["result_json"]["company_or_client_name"]) > 5
    assert response_dict["result_json"]["ticket_category"] == "AVR or DOA or HWS"
    assert response_dict["result_json"]["command_number"][0:2] == "FR"

def test_client_extract_structured_data_pk_list():
    file = "test/samples/pk-list-1.pdf"

    response = client.extract_structured_data(file=file, preset="pk-list", extraction_mode="precise")
    assert response["message"] == "Content Submitted. Data extract task created."
    ValueStorage.job_uuid_pk_list = response["job_uuid"]


def test_client_get_extract_structured_data_job_pk_list():
    time.sleep(15)
    response = client.get_extract_structured_data_job(ValueStorage.job_uuid_pk_list)
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["status"] in ["initialized", "processing", "completed"]
    assert response_dict["result_json"]["pk_list"][0]["invoice_no"] == "ABC272829"
    assert isinstance(response_dict["result_json"]["pk_list"][0]["list_part_number"], list)


def test_client_extract_structured_data_custom():
    string_content = "Salut j'ai un problême avec myportal"
    additional_instructions = "If myportal issue please name the ticket_category as MP_ACCESS"
    json_schema = json.loads("""{"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"ticket_category":{"type":"string"}},"required":["ticket_category"]}""")

    response = client.extract_structured_data(string_content=string_content, additional_instructions=additional_instructions, json_schema=json_schema)
    assert response["message"] == "Content Submitted. Data extract task created."
    ValueStorage.job_uuid_custom = response["job_uuid"]

def test_client_get_extract_structured_data_job_custom():
    time.sleep(15)
    response = client.get_extract_structured_data_job(ValueStorage.job_uuid_custom)
    assert response is not None
    response_dict = response.model_dump()
    assert response_dict["status"] in ["initialized", "processing", "completed"]
    assert response_dict["result_json"]["ticket_category"] == "MP_ACCESS"

def test_clean_up_after_test():
    response = client.revoke_api_key(
        api_key_to_revoke=ValueStorage.api_key["api_key"], creator_id="streamlit_userid"
    )
    filters = {
        "operator": "AND",
        "conditions": [
            {
                "field": "meta.pythia_document_category",
                "operator": "==",
                "value": "category2",
            }
        ],
    }
    response_doc_delete = client.delete_docs_by_filters(filters=filters)
    assert response is not None
    assert response_doc_delete is not None
