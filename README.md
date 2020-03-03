# dockerized bitcoind regtest

```shell
docker-compose build
docker-compose up
```

after completion of above steps you will have two bitcoind nodes on localhost:19001 and 19002
and flask app on localhost:19000 which will continuously call generate command on both nodes
