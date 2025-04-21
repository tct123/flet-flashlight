import asyncio

import flet as ft

__all__ = ["Flashlight"]

from .exceptions import *


@ft.control("Flashlight")
class Flashlight(ft.Service):
    """
    A control to use FlashLight. Works on iOS and Android. Based on torch_light Flutter widget (https://pub.dev/packages/torch_light).

    Flashlight control is non-visual and should be added to `page.overlay` list.

    Example:
    ```
    import flet as ft

    import flet_flashlight as ffl

    def main(page: ft.Page):
        flashLight = ffl.Flashlight()
        page.overlay.append(flashLight)
        page.add(
            ft.TextButton("toggle", on_click: lambda _: flashlight.toggle())
        )

    ft.app(target=main)
    ```

    """

    turned_on = False
    on_error: ft.OptionalControlEventCallable = None

    async def turn_on_async(self):
        r = await self._invoke_method_async("on")
        if r is True:
            self.turned_on = True
        else:  # error occured
            error_type = r.get("error_type")
            error_msg = r.get("error_msg")
            if error_type == "EnableTorchExistentUserException":
                raise FlashlightEnableExistentUserException(error_msg)
            elif error_type == "EnableTorchNotAvailableException":
                raise FlashlightEnableNotAvailableException(error_msg)
            else:
                raise FlashlightEnableException(error_msg)

    def turn_on(self):
        asyncio.create_task(self.turn_on_async())

    async def turn_off_async(self):
        r = await self._invoke_method_async("off")
        if r is True:
            self.turned_on = False
        else:  # error occured
            error_type = r.get("error_type")
            error_msg = r.get("error_msg")
            if error_type == "DisableTorchExistentUserException":
                raise FlashlightDisableExistentUserException(error_msg)
            elif error_type == "DisableTorchNotAvailableException":
                raise FlashlightDisableNotAvailableException(error_msg)
            else:
                raise FlashlightDisableException(error_msg)

    def turn_off(self):
        asyncio.create_task(self.turn_off_async())

    async def toggle_async(self):
        if self.turned_on:
            await self.turn_off_async()
        await self.turn_on_async()

    def toggle(self):
        asyncio.create_task(self.toggle_async())

    async def is_available_async(self):
        r = await self._invoke_method_async("is_available")
        if r is bool:
            return r
        else:  # error occured
            error_msg = r.get("error_msg")
            raise FlashlightException(error_msg)
