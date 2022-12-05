from fastapi import APIRouter

from app.services.scrape import get_price

router = APIRouter()


@router.get("/prices")
async def get_prices(
        product: str
) -> dict:
    try:
        flipkart_data, amazon_data = get_price(product)

        flipkart_data_ = []
        amazon_data_ = []

        for each in flipkart_data:
            flipkart_data_.append({
                'name': each,
                'price': flipkart_data[each][0],
                'link': flipkart_data[each][1]
            })
        for each in amazon_data:
            amazon_data_.append({
                'name': each,
                'price': amazon_data[each][0],
                'link': amazon_data[each][1]
            })

        data = {
            'flipkart': flipkart_data_,
            'amazon': amazon_data_
        }
        return {'message': 'success', 'data': data}
    except Exception as e:
        print(e)
        return {'message': 'error', 'data': ''}
