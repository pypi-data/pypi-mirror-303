# create by @xtdevs

class LoopAutomatic:
    @classmethod
    async def start_running_loop(cls, sessions, ClientClass) -> None:
        for i, data in enumerate(sessions):
            yield i, data

    @classmethod
    def _device_system(cls, **args):
        system_model = {
            "app_version": args.get("app_version", "1.0"),
            "device_model": args.get("device_model", "GenericDevice"),
            "system_version": args.get("system_version", "1.0")
        }
        return system_model

    @classmethod
    async def run_until_complete(
        cls,
        sessions,
        ClientClass,
        error_exceptions=None,
        logs=None,
        my_api_id=None,
        my_api_hash=None,
        plugins_dir=None,
        is_token: bool = False,
        **args
    ) -> None:
        get_model = cls._device_system(**args)
        if error_exceptions is None:
            error_exceptions = (Exception,)
        async for i, data in cls.start_running_loop(sessions, ClientClass):
            if is_token:
                bot_token_str = data.get("bot_token")
                client = ClientClass(
                    api_id=my_api_id,
                    api_hash=my_api_hash,
                    bot_token=bot_token_str,
                    app_version=get_model["app_version"],
                    device_model=get_model["device_model"],
                    system_version=get_model["system_version"],
                    plugins=dict(root=plugins_dir),
                )
            else:
                api_id = data.get("api_id")
                api_hash = data.get("api_hash")
                session_str = data.get("session")
                client = ClientClass(
                    api_id=api_id,
                    api_hash=api_hash,
                    session_string=session_str,
                    app_version=get_model["app_version"],
                    device_model=get_model["device_model"],
                    system_version=get_model["system_version"],
                    plugins=dict(root=plugins_dir)
                )
            try:
                await client.start()
                get_me = await client.get_me()
            except error_exceptions as e:
                if logs:
                    logs.error(f"Error on session {i + 1}: {str(e)}")
                continue
            if logs:
                logs.info(f"Starting: {i + 1} {get_me.first_name}")
            else:
                print(f"Starting: {i + 1} {get_me.first_name}")
