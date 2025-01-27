from typing import Optional
from fastapi import FastAPI, Form, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from handler.supplier import SupplierHandler
from fastapi.responses import JSONResponse

# FastAPI instance
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/PartApp/suppliers")
def get_all_suppliers(
    scity: Optional[str] = Query(None),  # Example query parameter for search
):
    supplier_handler = SupplierHandler()
    if scity:
        return supplier_handler.searchSuppliers(scity)
    return supplier_handler.getAllSuppliers()


@app.post("/PartApp/suppliers")
def create_supplier_from_form(
    sname: str = Form(), # form data-type request param
    scity: str = Form(),
    sphone: str = Form(),
):
    supplier_handler = SupplierHandler()
    return supplier_handler.insertSupplier(sname, scity, sphone)

@app.api_route('/PartApp/suppliers/{sid}',
           methods=['GET', 'PUT', 'DELETE']) # multi http method style
def getSupplierById(request: Request,sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return JSONResponse(content="Method not allowed", status_code=405)





