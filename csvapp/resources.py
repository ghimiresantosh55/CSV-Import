from import_export import resources
from src.csvapp.models import Customer

class CustomerResource(resources.ModelResource):
    class meta:
        model=Customer