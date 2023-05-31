from server.application import app
from src.business_model.recommender.BookLoader import BookLoader
from src.business_model.recommender.Recommender import Recommender


@app.get("/recommendation", tags=["Recommendation"])
async def recommend(book_id: int):
    books = BookLoader()

    recommendations = Recommender(books).run(book_id)

    return {
        "access_token": "",
        "message": "Success",
        "status_code": 200,
        "content": {
            "recommendations": recommendations
        },
    }
