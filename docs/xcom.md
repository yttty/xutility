# XCOM

The Websocket server and client for inter-process communication.

⚠️ CAVEAT: do not use it for exchange websocket streaming.

### Uasge

- Check the [examples](./examples) directory

### Data Transmission Protocol:
- Request:
    ```
    {
        "req_type": self._req_type,
        "ts": current_us(),
        "data": ..., // any orjson serializable obj
    }
    ```

- Success Rspsponse: returns `data` field and None
    ```
    {
        "ts": current_us(),
        "data": ..., // any orjson serializable obj
    }
    ```

- Unsuccess Rspsponse: returns None and `err_msg` field
    ```
    {
        "ts": current_us(),
        "err_msg": "some error msg",
    }
    ```

- Communication issues: returns None and `msg` returned by _raw_send (No rsp data)
