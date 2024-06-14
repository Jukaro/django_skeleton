FROM alpine:3.18

RUN apk update && apk upgrade
RUN apk add --no-cache python3 py3-pip

COPY --chmod=777 tools/* .

RUN pip install --no-cache-dir -r requirements
RUN rm requirements

WORKDIR /app

ENTRYPOINT [ "sh", "/start.sh" ]
# ENTRYPOINT [ "sleep", "infinity" ]
# ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
