from mosip_auth_sdk.models import DemographicsModel
from mosip_auth_sdk import MOSIPAuthenticator
from dynaconf import Dynaconf
from fastapi import FastAPI
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

config = Dynaconf(settings_files=["./config.toml"], environments=False)
authenticator = MOSIPAuthenticator(config=config)

# yes/no auth
demographics_data = DemographicsModel(dob="1997/09/12")
@app.post("/authenticate")
async def auth():
    logger.info("Attempting to authenticate")
    response = authenticator.auth(
        individual_id="5408602380",
        individual_id_type="UIN",
        demographic_data=demographics_data,
        consent=True,
    )
    response_body = response.json()
    logger.info(f"RESPONSE: {response_body}")
    return response_body

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)