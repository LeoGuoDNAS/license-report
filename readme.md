# License Report
Report Active Sampro Licenses Daily
## Deployment
AWS Lambda + AWS EventBridge (for daily invocation)
#### Install Packges
pip install -t dep -r requirements.txt
#### Zip Deps
Compress-Archive -Path .\\dep\\* -DestinationPath .\\lambda_artifact.zip -Force
#### Zip Py Files
Compress-Archive -Path .\\auth.py -Update -DestinationPath .\\lambda_artifact.zip