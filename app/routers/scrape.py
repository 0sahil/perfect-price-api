from fastapi import APIRouter, Depends

from app.services.scrape import get_price
import requests

router = APIRouter()


@router.get("/prices")
async def get_prices(
        product: str
) -> dict:
    flipkart_data, amazon_data = get_price(product)

    data = {
        'flipkart': flipkart_data,
        'amazon': amazon_data
    }

    return {'message': 'success', 'data': data}
