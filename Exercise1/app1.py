import math
from flask import Flask, request

app = Flask("Trigonometry")
@app.route("/trig/<func>/")
def trig(func):
    try:
        args = request.args
        angle = float(args["angle"])
        unit = args.get("unit", "radian")
        if unit not in ["radian", "degree"]:
            response = ("Invalid query parameter value(s)", 400)
        else:
            if unit == "degree":
                angle = math.radians(angle)
            
            operations = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan
            }
            
            if func in operations:
                result = operations[func](angle)
                response = (f"{result}", 200)
            else:
                response = ("Operation not found", 404)
    except KeyError:
        response = ("Missing query parameter: angle", 400)
    except ValueError:
        response = ("Invalid query parameter value(s)", 400)
    
    return response
