try:
    import pkg_resources

    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil

    __path__ = pkgutil.extend_path(__path__, __name__)

from wiser.gcloud.firestore.services.firestore_service import Firestore
from wiser.gcloud.firestore.types.query import (
    FirestoreQueryBuilder,
    FirestoreQueryCondition,
    FirestoreQueryDirection,
)
from wiser.gcloud.firestore.types.document import FirestoreDocumentBuilder
from wiser.gcloud.firestore.types.collection import FirestoreCollectionBuilder

__all__ = [
    "Firestore",
    "FirestoreQueryBuilder",
    "FirestoreQueryDirection",
    "FirestoreQueryCondition",
    "FirestoreDocumentBuilder",
    "FirestoreCollectionBuilder",
]
