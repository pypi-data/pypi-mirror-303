from __future__ import annotations

import functools
from abc import ABC
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Concatenate, Type, cast

from tibia import maybe, pipeline


@dataclass(slots=True)
class AsyncResult[_TOk, _TErr]:
    value: Awaitable[Result[_TOk, _TErr]]

    async def unwrap(self):
        return (await self.value).unwrap()

    async def unwrap_or(self, other: _TOk | Callable[[], _TOk]):
        return (await self.value).unwrap_or(other)

    def unwrap_as_pipeline(self):
        return pipeline.AsyncPipeline(self.unwrap())

    def unwrap_as_pipeline_or(self, other: _TOk | Callable[[], _TOk]):
        return pipeline.AsyncPipeline(self.unwrap_or(other))

    def unwrap_as_maybe(self):
        async def _unwrap_as_maybe():
            return (await self.value).unwrap_as_maybe()

        return maybe.AsyncMaybe(_unwrap_as_maybe())

    def unwrap_as_maybe_or(self, other: _TOk | Callable[[], _TOk]):
        async def _unwrap_as_maybe_or():
            return (await self.value).unwrap_as_maybe_or(other)

        return maybe.AsyncMaybe(_unwrap_as_maybe_or())

    def map[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TResult, _TErr]:
        async def _map():
            return (await self.value).map(func, *args, **kwargs)

        return AsyncResult(_map())

    def map_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TResult, _TErr]:
        async def _map_async() -> Result[_TResult, _TErr]:
            result = await self.value

            if isinstance(result, Ok):
                return Ok(await func(result.value, *args, **kwargs))
            return cast(Result[_TResult, _TErr], result)

        return AsyncResult(_map_async())

    async def then[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        return (await self.value).then(func, *args, **kwargs)

    async def then_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        return await func((await self.value).unwrap(), *args, **kwargs)

    async def then_or[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        other: _TResult | Callable[[], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        return (await self.value).then_or(func, other, *args, **kwargs)

    async def then_or_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        other: _TResult | Callable[[], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        result = await self.value
        if isinstance(result, Ok):
            return await func(result.value, *args, **kwargs)

        return cast(_TResult, other() if isinstance(other, Callable) else other)

    def otherwise[**_ParamSpec, _TNewErr](
        self,
        func: Callable[Concatenate[_TErr, _ParamSpec], _TNewErr],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TOk, _TNewErr]:
        async def _otherwise():
            _result = await self.value

            if isinstance(_result, Err):
                return Err(func(_result.value, *args, **kwargs))

            return _result

        return AsyncResult(_otherwise())

    def otherwise_async[**_ParamSpec, _TNewErr](
        self,
        func: Callable[Concatenate[_TErr, _ParamSpec], Awaitable[_TNewErr]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TOk, _TNewErr]:
        async def _otherwise_async():
            _result = await self.value

            if isinstance(_result, Err):
                return Err(await func(_result.value, *args, **kwargs))

            return _result

        return AsyncResult(_otherwise_async())

    def recover(self, other: _TOk | Callable[[], _TOk]) -> AsyncResult[_TOk, _TErr]:
        async def _recover():
            return (await self.value).recover(other)

        return AsyncResult(_recover())


class Result[_TOk, _TErr](ABC):
    def as_ok(self) -> Ok[_TOk]:
        if not isinstance(self, Ok):
            raise ValueError("cannot cast to Ok")

        return self

    def as_err(self) -> Err[_TErr]:
        if not isinstance(self, Err):
            raise ValueError("cannot cast to Err")

        return self

    def is_ok(self):
        return isinstance(self, Ok)

    def is_err(self):
        return isinstance(self, Err)

    def unwrap(self) -> _TOk:
        if not isinstance(self, Ok):
            err_result = cast(Err[_TErr], self)
            raise ValueError("error result", err_result.value)

        return self.value

    def unwrap_or(self, other: _TOk | Callable[[], _TOk]) -> _TOk:
        if not isinstance(self, Ok):
            return cast(_TOk, other() if isinstance(other, Callable) else other)

        return self.value

    def unwrap_as_pipeline(self) -> pipeline.Pipeline[_TOk]:
        return pipeline.Pipeline(self.unwrap())

    def unwrap_as_pipeline_or(
        self, other: _TOk | Callable[[], _TOk]
    ) -> pipeline.Pipeline[_TOk]:
        return pipeline.Pipeline(self.unwrap_or(other))

    def unwrap_as_maybe(self) -> maybe.Maybe[_TOk]:
        return maybe.Some(self.unwrap())

    def unwrap_as_maybe_or(self, other: _TOk | Callable[[], _TOk]) -> maybe.Maybe[_TOk]:
        return maybe.Some(self.unwrap_or(other))

    def map[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> Result[_TResult, _TErr]:
        if isinstance(self, Ok):
            return Ok(func(self.value, *args, **kwargs))

        return cast(Result[_TResult, _TErr], self)

    def map_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TResult, _TErr]:
        async def _map_async() -> Result[_TResult, _TErr]:
            if isinstance(self, Ok):
                return Ok(await func(self.value, *args, **kwargs))

            return cast(Result[_TResult, _TErr], self)

        return AsyncResult(_map_async())

    def then[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        value = self.unwrap()
        return func(value, *args, **kwargs)

    def then_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> Awaitable[_TResult]:
        async def _then_async():
            value = self.unwrap()
            return await func(value, *args, **kwargs)

        return _then_async()

    def then_or[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], _TResult],
        other: _TResult | Callable[[], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> _TResult:
        return self.map(func, *args, **kwargs).unwrap_or(other)

    def then_or_async[**_ParamSpec, _TResult](
        self,
        func: Callable[Concatenate[_TOk, _ParamSpec], Awaitable[_TResult]],
        other: _TResult | Callable[[], _TResult],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> Awaitable[_TResult]:
        async def _then_or_async():
            if isinstance(self, Ok):
                return await func(self.value, *args, **kwargs)

            return cast(_TResult, other() if isinstance(other, Callable) else other)

        return _then_or_async()

    def otherwise[**_ParamSpec, _TNewErr](
        self,
        func: Callable[Concatenate[_TErr, _ParamSpec], _TNewErr],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> Result[_TOk, _TNewErr]:
        if isinstance(self, Err):
            _err = cast(Err[_TErr], self)
            return Err(func(_err.value, *args, **kwargs))

        return self  # type: ignore

    def otherwise_async[**_ParamSpec, _TNewErr](
        self,
        func: Callable[Concatenate[_TErr, _ParamSpec], Awaitable[_TNewErr]],
        *args: _ParamSpec.args,
        **kwargs: _ParamSpec.kwargs,
    ) -> AsyncResult[_TOk, _TNewErr]:
        async def _otherwise_async() -> Result[_TOk, _TNewErr]:
            if isinstance(self, Err):
                _err = cast(Err[_TErr], self)
                return Err(await func(_err.value, *args, **kwargs))

            return self  # type: ignore

        return AsyncResult(_otherwise_async())

    def recover(self, other: _TOk | Callable[[], _TOk]) -> Result[_TOk, _TErr]:
        if isinstance(self, Err):
            return Ok(cast(_TOk, other() if isinstance(other, Callable) else other))

        return self


@dataclass(slots=True)
class Ok[_TOk](Result[_TOk, Any]):
    value: _TOk

    def with_err[_TErr](self, _: Type[_TErr]) -> Result[_TOk, _TErr]:
        return cast(Result[_TOk, _TErr], self)


@dataclass(slots=True)
class Err[_TErr](Result[Any, _TErr]):
    value: _TErr

    def with_ok[_TOk](self, _: Type[_TOk]) -> Result[_TOk, _TErr]:
        return cast(Result[_TOk, _TErr], self)


def result_returns[**_ParamSpec, _TOk](
    func: Callable[_ParamSpec, _TOk],
) -> Callable[_ParamSpec, Result[_TOk, Exception]]:
    @functools.wraps(func)
    def _result_returns_async(
        *args: _ParamSpec.args, **kwargs: _ParamSpec.kwargs
    ) -> Result[_TOk, Exception]:
        try:
            return Ok(func(*args, **kwargs))
        except Exception as exc:
            return Err(exc)

    return _result_returns_async  # type: ignore


def result_returns_async[**_ParamSpec, _TOk](
    func: Callable[_ParamSpec, Awaitable[_TOk]],
) -> Callable[_ParamSpec, AsyncResult[_TOk, Exception]]:
    @functools.wraps(func)
    def _result_returns_async(
        *args: _ParamSpec.args, **kwargs: _ParamSpec.kwargs
    ) -> AsyncResult[_TOk, Exception]:
        async def __result_returns_async() -> Result[_TOk, Exception]:
            try:
                return Ok(await func(*args, **kwargs))
            except Exception as exc:
                return Err(exc)

        return AsyncResult(__result_returns_async())

    return _result_returns_async  # type: ignore


def result_unwrap[_TOk](result: Result[_TOk, Any]) -> _TOk:
    return result.unwrap()


def result_is_ok(result: Result[Any, Any]) -> bool:
    return result.is_ok()


def result_is_err(result: Result[Any, Any]) -> bool:
    return result.is_err()


def result_as_err[_TErr](result: Result[Any, _TErr]) -> Err[_TErr]:
    return result.as_err()


def result_as_ok[_TOk](result: Result[_TOk, Any]) -> Ok[_TOk]:
    return result.as_ok()
