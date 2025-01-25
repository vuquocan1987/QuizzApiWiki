from flask import Flask, request, jsonify
# import UnsupporttedMediaType


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class StorageItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    location = db.Column(db.String(64), nullable=False)

    product = db.relationship("Product", back_populates="storage_items")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(64), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    storage_items = db.relationship("StorageItem", back_populates="product")

@app.route("/products/add/",methods=["POST"])
def add_product():
    try:
        json = request.json
        handle = json["handle"]
        price = json["price"]
        weight = json["weight"]
        if not (isinstance(price, (int, float)) and isinstance(weight, (int, float))):
            return ("Weight and price must be numbers", 400)
        
        
        product = Product(handle=handle, price=price, weight=weight)
        db.session.add(product)
        db.session.commit()
    except KeyError:
        return ("Missing query parameter(s)", 400)
    except IntegrityError:
        return ("Handle already exists", 409)
    return "Product added successfully", 201
    

@app.route("/storage/<product>/add/", methods=["POST"])
def add_storage_item(product):
    try:
        json = request.json
        if json is None:
            return ("Request content type must be JSON", 415)
        qty = json["qty"]
        location = json["location"]
        if not isinstance(qty, int):
            return ("Qty must be an integer", 400)
        if json is None or not all([qty, location]):
            return ("Request content type must be JSON", 415)
        
        product = Product.query.filter_by(handle=product).first()
        if product is None:
            return ("Product not found", 404)
        
        storage_item = StorageItem(qty=qty, location=location, product=product)
        db.session.add(storage_item)
        db.session.commit()
    except KeyError:
        return ("Missing query parameter(s)", 400)
    except IntegrityError:
        return ("Product already exists", 409)
    return "Storage item added successfully", 201
    
@app.route("/storage/", methods=["GET"])
def get_storage():
    storage_items = StorageItem.query.all()
    result = {}
    for item in storage_items:
        handle = item.product.handle
        if handle not in result:
            product = db.session.query(Product).filter(Product.handle == handle).first()
            result[handle] = {"price": product.price, "weight": product.weight,"inventory": []}
        result[handle]["inventory"].append([item.location,item.qty])
    # group by product handle
    final_result = []
    for handle, data in result.items():
        final_result.append({"handle": handle, **data})
    return jsonify(final_result),200
