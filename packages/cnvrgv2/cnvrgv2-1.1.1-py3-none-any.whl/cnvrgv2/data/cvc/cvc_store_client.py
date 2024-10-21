from cnvrgv2.data.clients.storage_client_factory import storage_client_factory
from cnvrgv2.data.cvc.cvc_store import CvcStore
from cnvrgv2.data.cvc.error_messages import CVC_STORE_CREATE_FAULTY_NAME, CVC_STORE_GET_FAULTY_NAME
from cnvrgv2.data.cvc.routes import CVC_STORE_BASE, CVC_STORES_BASE
from cnvrgv2.errors import CnvrgArgumentsError
from cnvrgv2.proxy import HTTP, Proxy
from cnvrgv2.utils.json_api_format import JAF


class CvcStoreClient:
    def __init__(self, cvc_base_url, cnvrg_dataset):
        """
        Constructor for the cvc service
        @param cvc_base_url: Base url of the cvc service
        @param cnvrg_dataset: A cnvrg dataset object. Used to get storage credentials
        """
        self._proxy = Proxy(domain=cvc_base_url)
        # The following line is a patch for phase1 and needs to be reorganized in phase 2
        self._storage_client = storage_client_factory(refresh_function=cnvrg_dataset.storage_meta_refresh_function())

    def cvc_create_store(self, name):
        """
        Create a new store in cvc service
        @param name: String. Name for the new store
        @return: The attributes of the new cvc store
        """
        if not name or not isinstance(name, str):
            raise CnvrgArgumentsError(CVC_STORE_CREATE_FAULTY_NAME)

        attributes = {
            "name": name
        }

        response = self._proxy.call_api(
            route=CVC_STORES_BASE,
            http_method=HTTP.POST,
            payload=JAF.serialize(type="cvc", attributes=attributes)
        )

        return CvcStore(self._proxy, self._storage_client, response.attributes)

    def cvc_get_store(self, slug):
        """
        Get a store from cvc service
        @param slug: String. slug of the store to get
        @return: The attributes of the cvc store
        """
        if not slug or not isinstance(slug, str):
            raise CnvrgArgumentsError(CVC_STORE_GET_FAULTY_NAME)

        response = self._proxy.call_api(
            route=CVC_STORE_BASE.format(slug),
            http_method=HTTP.GET
        )

        return CvcStore(self._proxy, self._storage_client, response.attributes)
