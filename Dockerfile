FROM python:3.10.5-buster

WORKDIR /KGUB/

RUN apt-get update -y && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["python3", "-m", "KGUB"]