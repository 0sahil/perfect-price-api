from fastapi import APIRouter

from app.services.scrape import get_price

router = APIRouter()


@router.get("/prices")
async def get_prices(
        product: str
) -> dict:
    try:
        flipkart_data, amazon_data = get_price(product)
        data = {
            'flipkart': flipkart_data,
            'amazon': amazon_data
        }
        return {'message': 'success', 'data': data}
    except Exception as e:
        print(e)
        return {'message': 'error', 'data': ''}
