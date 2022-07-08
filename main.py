
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import DrawingOptions
import io

from flask import send_file

def gen_png_from_smiles(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    # grab the smiles string from the url parameter
    # this should be validated, etc., but for now this will prove out the concept
    smi = request.args.get('smiles')

    # log value for debugging
    print(smi)
    
    # create molecule object
    mol = Chem.MolFromSmiles(smi)

    # draw molcule as PIL
    pil_img = Draw.MolsToImage([mol])

    # create buffer 
    img_io = io.BytesIO()

    # write image to buffer
    pil_img.save(img_io, "PNG", subsampling=0, quality=95)

    # seek to byte0 
    img_io.seek(0)

    # return image
    return send_file(img_io, mimetype="image/png")
    
