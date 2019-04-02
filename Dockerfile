FROM python:3.7

COPY Pipfile Pipfile.lock Makefile ./

RUN make install-prod

COPY . .

CMD ["make", "run-prod"]
