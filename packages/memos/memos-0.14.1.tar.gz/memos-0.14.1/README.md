# Memos

A project to index everything to make it like another memory. The project contains two parts:

1. `screen recorder`: which takes screenshots every 5 seconds and saves them to `~/.memos/screenshots` by default.
2. `memos server`: a web service that can index the screenshots and other files, providing a web interface to search the records.

There is a product called [Rewind](https://www.rewind.ai/) that is similar to memos, but memos aims to give you control over all your data.

## Install

### Install Typesense

```bash
export TYPESENSE_API_KEY=xyz

mkdir "$(pwd)"/typesense-data

docker run -d -p 8108:8108 \
    -v"$(pwd)"/typesense-data:/data typesense/typesense:27.0 \
    --add-host=host.docker.internal:host-gateway \
    --data-dir /data \
    --api-key=$TYPESENSE_API_KEY \
    --enable-cors
```

### Install Memos

```bash
pip install memos
```

## How to use

To use memos, you need to initialize it first. Make sure you have started `typesense`.

### 1. Initialize Memos

```bash
memos init
```

This will create a folder `~/.memos` and put the config file there.

### 2. Start Screen Recorder

```bash
memos-record
```

This will start a screen recorder, which will take screenshots every 5 seconds and save it at `~/.memos/screenshots` by default.

### 3. Start Memos Server

```bash
memos serve
```

This will start a web server, and you can access the web interface at `http://localhost:8080`.
The default username and password is `admin` and `changeme`.

### Index the screenshots

```bash
memos scan
memos index
```

Refresh the page, and do some search.
