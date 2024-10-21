from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route
import os

# Define a simple handler to serve the HTML file
async def homepage(request):
    # Return the index.html file located in the static/ folder
    file_path = os.path.join(os.path.dirname(__file__), 'static', 'index.html')
    return FileResponse(file_path)

# Define the routes
routes = [
    Route("/", homepage),
]

# Create the ASGI app
app = Starlette(routes=routes)

if __name__ == "__main__":
    import uvicorn
    # Run the app with hot reloading enabled for development
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
