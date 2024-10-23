### Build instructions

Run the following command and be sure to add the actual path of your github personal access token

```
docker build --tag <<{{TOOL_NAME}}>> --secret id=token,src=</path/to/token> --platform=linux/x86_64 .
```