from fastapi import APIRouter, Response, HTMLResponse, PlainTextResponse, Form

router = APIRouter(prefix='/product',tags=['product'])

products = ['watch','camera','phone']

@router.get('/all')
def get_all_products():
    data = " ".join(products)
    return Response(content=data,media_type="text/plain")

@router.post('/new')
def create_product(name: str =Form(...)):
    products.append(name)
    return products


@router.get('/{id}',responses={
     200:{
        'content':{
            'text/html':{
                'example':'<div>Product</div' 
            }
        },
        'description':'Return HTML for an object'
    },
    404:{
        'content':{
            'text/plain':{
                'example':'Product not available' 
            }
        },
        'description':'A clear text error message'
    }
})
def get_product(id:int):
    if id > len(products):
        out = f"Product not found , please enter a valid {id}"
        return PlainTextResponse(content=out,media_type="text/plain")
        product = products[id]
        out = f'''
            <head>
                <style>
                .product {{
                    width: 50px;
                    height: 30px;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center
                }}
                </style>
            </head>
            <div class="product">{product}</div>  
        '''

        return HTMLResponse(content=out,media_type='text/html')