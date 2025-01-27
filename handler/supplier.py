from dao.supplier import SupplierDAO
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class SupplierHandler:
    def insertSupplier(self, sname,scity,sphone):
        if sname and scity and sphone:
            dao = SupplierDAO()
            sid = dao.insert(sname, scity, sphone)
            return JSONResponse(content={'sid':sid}, status_code=201)
        else:
            raise HTTPException(status_code=400, detail="Malformed post request")

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        return JSONResponse(content={'Suppliers':suppliers_list}, status_code=200)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        supplier = dao.getSupplierById(sid)
        if not supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
        else:
            return JSONResponse(content={'Supplier':supplier}, status_code=200)

    def getPartsBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            raise HTTPException(status_code=404, detail="Supplier not found")
        parts_list = dao.getPartsBySupplierId(sid)
        return JSONResponse(content={'PartsSupply':parts_list}, status_code=200)

    def searchSuppliers(self, city):
            if city:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByCity(city)
                return JSONResponse(content={'Suppliers': supplier_list}, status_code=200)