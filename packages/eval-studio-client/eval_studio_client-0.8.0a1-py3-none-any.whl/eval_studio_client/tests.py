import dataclasses
import datetime
import json
from typing import List
from typing import Optional
from typing import Union

from eval_studio_client import api
from eval_studio_client import documents as d7s
from eval_studio_client import perturbators as p10s
from eval_studio_client.api import models


@dataclasses.dataclass
class TestCase:
    """Represents a single test case, which contains tested prompt, expected answer
    and set of constraints.

    Attributes:
        key (str): Generated ID of the test case.
        prompt (str): Prompt of the test case.
        answer (str): Expected answer of the test case.
        constraints (List[str]): String tokens expected in the actual answer.
            Note: all of the constraints in the list are concatenated using AND
            operator, which means actual answer need to contain all of the tokens.
        create_time (datetime): Timestamp of the test case creation.
        update_time (datetime): Timestamp of the last test case update.
    """

    key: str
    prompt: str
    answer: str
    constraints: List[str]
    condition: str
    create_time: Optional[datetime.datetime] = None
    update_time: Optional[datetime.datetime] = None

    def to_api_proto(self) -> models.V1alphaTestCase:
        """Converts the client TestCase to an API TestCase."""
        return models.V1alphaTestCase(
            prompt=self.prompt,
            answer=self.answer,
            constraints=self.constraints,
            condition=self.condition,
        )

    @staticmethod
    def _from_api_test_case(api_test_case: models.V1alphaTestCase) -> "TestCase":
        return TestCase(
            key=api_test_case.name or "",
            prompt=api_test_case.prompt or "",
            answer=api_test_case.answer or "",
            constraints=api_test_case.constraints or [],
            condition=api_test_case.condition or "",
        )


@dataclasses.dataclass
class Test:
    """Represents a test, which contains a set of test cases and optionally
    also documents for evaluating RAG systems.

    Attributes:
        key (str): Generated ID of the test.
        name (str): Name of the test.
        description (str): Description of the test.
        create_time (datetime): Timestamp of the test creation.
        update_time (datetime): Timestamp of the last test update.
    """

    key: str
    name: str
    description: str
    _document_names: List[str]
    create_time: Optional[datetime.datetime] = None
    update_time: Optional[datetime.datetime] = None
    _client: Optional[api.ApiClient] = None

    def __post_init__(self):
        if self._client:
            self._test_api = api.TestServiceApi(self._client)
            self._test_case_api = api.TestCaseServiceApi(self._client)
            self._document_api = api.DocumentServiceApi(self._client)

    @property
    def test_cases(self) -> List[TestCase]:
        """Retrieves all test cases in the test."""
        res = self._test_case_api.test_case_service_list_test_cases(self.key)
        if res and res.test_cases:
            return [TestCase._from_api_test_case(tc) for tc in res.test_cases]

        return []

    @property
    def documents(self) -> List[d7s.Document]:
        """Retrieves all documents attached to the test."""
        if not self._document_names:
            return []

        res = self._document_api.document_service_batch_get_documents(
            self._document_names
        )
        if res and res.documents:
            return [
                d7s.Document._from_api_document(d, self._client) for d in res.documents
            ]

        return []

    def perturb(
        self,
        new_test_name: str,
        perturbators: Union[p10s.Perturbator, str, List[Union[p10s.Perturbator, str]]],
        new_test_description: str = "",
    ) -> "Test":
        """Creates new Test by perturbing this test using the given Perturbators.

        Args:
            new_test_name (str): Name of the newly created test.
            perturbators (Perturbator, List[Perturbator], str or List[str]): List of Perturbators or
                their keys used to perturbate this Test.
            new_test_description (str): Optional description of the newly created test.
        """

        if self._client is None:
            raise RuntimeError("Client is not set.")

        if not new_test_name:
            raise ValueError("New test name must be provided.")

        if not perturbators:
            raise ValueError("Perturbators must be provided.")

        if isinstance(perturbators, (p10s.Perturbator, str)):
            perturbators_to_run = [perturbators]
        else:
            perturbators_to_run = perturbators

        configs = [_PerturbatorConfiguration(p) for p in perturbators_to_run]

        req = models.TestServicePerturbTestRequest(
            perturbatorConfigurations=[c.to_api_proto() for c in configs],
            newTestDisplayName=new_test_name,
            newTestDescription=new_test_description,
        )
        resp = self._test_api.test_service_perturb_test(self.key, req)
        return Test._from_api_test(resp.test, self._client)

    def delete(self, force=False):
        """Deletes the test.

        Args:
            force (bool): If True, test cases will be deleted as well.
        """
        self._test_api.test_service_delete_test(self.key, force=force)

    def create_test_case(
        self,
        prompt: str,
        answer: str,
        constraints: Optional[List[str]] = None,
        condition: str = "",
    ) -> Optional[TestCase]:
        """Creates a new test case in the test.

        Args:
            prompt (str): Prompt of the test case.
            answer (str): Expected answer of the test case.
            constraints (List[str]): String tokens expected in the actual answer.
                Note: all of the constraints in the list are concatenated using AND
                operator, which means actual answer need to contain all of the tokens.
            condition (str): Test case output condition, in a form logical expression.
                The format of the string is defined by the Google's filtering language.
                (ref. https://google.aip.dev/160#logical-operators)
        """
        case = TestCase(
            key="",
            prompt=prompt,
            answer=answer,
            constraints=constraints or [],
            condition=condition,
        )
        res = self._test_case_api.test_case_service_create_test_case(
            parent=self.key, test_case=case.to_api_proto()
        )
        if res and res.test_case:
            return TestCase._from_api_test_case(res.test_case)

        return None

    def remove_test_case(self, test_case_key: str):
        """Removes a test case from the test.

        Args:
            test_case_key (str): Resource name of the test case to be removed.
        """
        self._test_case_api.test_case_service_delete_test_case(test_case_key)

    def create_document(
        self, name: str, url: str, description: Optional[str] = None
    ) -> Optional[d7s.Document]:
        """Creates a new document and attaches it to the test.

        Args:
            name (str): Name of the document.
            url (str): URL of the document.
            description (str): Description of the document.
        """
        doc = d7s.Document("", name, description or "", url)
        res = self._document_api.document_service_create_document(doc.to_api_proto())
        if res and res.document:
            doc = d7s.Document._from_api_document(res.document, self._client)

        try:
            self.link_document(doc)
        except ValueError as err:
            raise RuntimeError("Failed to create the document.") from err
        except Exception as err:
            doc.delete()
            raise RuntimeError("Failed to link the document to the test.") from err

        return doc

    def link_document(self, document: d7s.Document):
        """Attaches an existing document to the test.

        Args:
            document (Document): Document to be attached to the test.
        """
        if not document.key:
            raise ValueError("Document must have a resource name.")

        self._document_names.append(document.key)
        try:
            self._test_api.test_service_update_test(
                test_name=self.key,
                test=models.RequiredTheTestToUpdate(documents=self._document_names),
            )
        except Exception as err:
            self._document_names.remove(document.key)
            raise RuntimeError("Failed to link the document to the test.") from err

    def unlink_document(self, document_key: str):
        """Deletes a document attached to the test.

        Args:
            document_key (str): Resource name of the document to be detached from the test.
        """
        try:
            self._document_names.remove(document_key)
        except ValueError as err:
            raise ValueError(
                f"Document {document_key} is not attached to the test."
            ) from err

        try:
            self._test_api.test_service_update_test(
                test_name=self.key,
                test=models.RequiredTheTestToUpdate(documents=self._document_names),
            )
        except Exception as err:
            self._document_names.append(document_key)
            raise RuntimeError("Failed to unlink the document from the test.") from err

    @staticmethod
    def _from_api_test(api_test: models.V1alphaTest, client: api.ApiClient) -> "Test":
        return Test(
            key=api_test.name or "",
            name=api_test.display_name or "",
            description=api_test.description or "",
            create_time=api_test.create_time,
            update_time=api_test.update_time,
            _document_names=api_test.documents or [],
            _client=client,
        )


class _Tests:
    def __init__(self, client: api.ApiClient):
        self._client = client
        self._api = api.TestServiceApi(client)

    def list(self) -> List[Test]:
        """Retrieves all user tests in the Eval Studio."""
        res = self._api.test_service_list_tests()
        if res and res.tests:
            return [Test._from_api_test(t, self._client) for t in res.tests]

        return []

    def create(
        self,
        name: str,
        description: Optional[str] = "",
        documents: Optional[List[d7s.Document]] = None,
    ) -> Optional[Test]:
        """Creates a new test in the Eval Studio.

        Args:
            name (str): Name of the test.
            description (str): Description of the test.
            documents (optional): List of `Document`s to be attached to the test.
        """
        _documents = [d.key for d in documents] if documents else None
        test = models.V1alphaTest(
            display_name=name, description=description, documents=_documents
        )
        res = self._api.test_service_create_test(test)
        if res and res.test:
            return Test._from_api_test(res.test, self._client)

        return None

    def delete(self, key: str):
        """Deletes the test with given resource name.

        Args:
            key (str): Resource name of the test to be deleted.
        """
        self._api.test_service_delete_test(key)

    def import_test_suite(
        self, test_suite: str, name_prefix: Optional[str] = None
    ) -> List[Test]:
        """Imports a list of tests (Test Suite) from a JSON.

        Args:
            test_suite (str): JSON string of the test suite.
            name_prefix (str): Optional prefix to name the imported tests.
        """
        req = models.V1alphaBatchImportTestsRequest(
            testsJson=test_suite, testDisplayNamePrefix=name_prefix or None
        )
        res = self._api.test_service_batch_import_tests(req)
        if res and res.tests:
            return [Test._from_api_test(t, self._client) for t in res.tests]

        return []


class _PerturbatorConfiguration:
    """Represents the configuration of a perturbator to use during the perturbation process.

    Attributes:
        perturbator (Perturbator or str): Perturbator to use or its key.
    """

    def __init__(self, perturbator: Union[p10s.Perturbator, str]):
        self.name = (
            perturbator.key
            if isinstance(perturbator, p10s.Perturbator)
            else perturbator
        )
        self.intensity = (
            perturbator.intensity
            if isinstance(perturbator, p10s.Perturbator)
            else p10s.PerturbatorIntensity.medium
        )
        self.params = (
            perturbator.params if isinstance(perturbator, p10s.Perturbator) else None
        )

    def to_api_proto(self) -> models.V1alphaPerturbatorConfiguration:
        """Converts the client PerturbatorConfiguration to an API PerturbatorConfiguration."""
        return models.V1alphaPerturbatorConfiguration(
            name=self.name,
            intensity=self.intensity.to_api_proto(),
            params=json.dumps(self.params) if self.params else None,
        )
