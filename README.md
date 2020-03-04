# dockerized bitcoind regtest

```shell
docker-compose build
docker-compose up
```

after completion of above steps you will have two bitcoind nodes ready for rpc calls on localhost:19001 and 19002
and flask app on localhost:19000 which will continuously call generate command on both nodes to keep chain goin

There's estimatesmartfee mode where flaskapp starts generating a high amount of transactions between nodes, for it to work you should set environment variable $ESMART_FEE=1


rpcuser=rpc
rpcpassword=x

examples of rpc calls:
```shell
curl --user rpc:x --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "estimatesmartfee", "params": [1] }' -H 'content-type: text/plain;' http://127.0.0.1:19002
curl --user rpc:x --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblockchaininfo"}' -H 'content-type: text/plain;' http://127.0.0.1:19001
```

