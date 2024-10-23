from ..exports import core
from ..intrinsics import _clamp, _decode_utf8, _encode_utf8, _load, _store
from ..types import Err, Ok, Result
import ctypes
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
import wasmtime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .. import Root

Error = core.Error
TypeId = int
@dataclass
class ReduceEntry:
    path: List[str]
    injection_data: str

@dataclass
class AuthProtocolOauth2:
    pass

@dataclass
class AuthProtocolJwt:
    pass

@dataclass
class AuthProtocolBasic:
    pass

AuthProtocol = Union[AuthProtocolOauth2, AuthProtocolJwt, AuthProtocolBasic]

@dataclass
class Auth:
    name: str
    protocol: AuthProtocol
    auth_data: List[Tuple[str, str]]

@dataclass
class QueryDeployParams:
    tg: str
    secrets: Optional[List[Tuple[str, str]]]

@dataclass
class FdkConfig:
    workspace_path: str
    target_name: str
    config_json: str
    tg_json: str

@dataclass
class FdkOutput:
    path: str
    content: str
    overwrite: bool

class Utils:
    component: 'Root'
    
    def __init__(self, component: 'Root') -> None:
        self.component = component
    def reduceb(self, caller: wasmtime.Store, fn_type_id: TypeId, entries: List[ReduceEntry]) -> Result[TypeId, Error]:
        vec9 = entries
        len11 = len(vec9)
        result10 = self.component._realloc0(caller, 0, 0, 4, len11 * 16)
        assert(isinstance(result10, int))
        for i12 in range(0, len11):
            e = vec9[i12]
            base0 = result10 + i12 * 16
            record = e
            field = record.path
            field1 = record.injection_data
            vec = field
            len5 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len5 * 8)
            assert(isinstance(result, int))
            for i6 in range(0, len5):
                e2 = vec[i6]
                base3 = result + i6 * 8
                ptr, len4 = _encode_utf8(e2, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 4, len4)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 0, ptr)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, len5)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 0, result)
            ptr7, len8 = _encode_utf8(field1, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 12, len8)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 8, ptr7)
        ret = self.component.lift_callee77(caller, _clamp(fn_type_id, 0, 4294967295), result10, len11)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[TypeId, Error]
        if load == 0:
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load13 & 0xffffffff)
        elif load == 1:
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr21 = load14
            len22 = load15
            result23: List[str] = []
            for i24 in range(0, len22):
                base16 = ptr21 + i24 * 8
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 0)
                load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 4)
                ptr19 = load17
                len20 = load18
                list = _decode_utf8(self.component._core_memory0, caller, ptr19, len20)
                result23.append(list)
            expected = Err(core.Error(result23))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def add_graphql_endpoint(self, caller: wasmtime.Store, graphql: str) -> Result[int, Error]:
        ptr, len0 = _encode_utf8(graphql, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee78(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[int, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def add_auth(self, caller: wasmtime.Store, data: Auth) -> Result[int, Error]:
        record = data
        field = record.name
        field0 = record.protocol
        field1 = record.auth_data
        ptr, len2 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        if isinstance(field0, AuthProtocolOauth2):
            variant = 0
        elif isinstance(field0, AuthProtocolJwt):
            variant = 1
        elif isinstance(field0, AuthProtocolBasic):
            variant = 2
        else:
            raise TypeError("invalid variant specified for AuthProtocol")
        vec = field1
        len11 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len11 * 16)
        assert(isinstance(result, int))
        for i12 in range(0, len11):
            e = vec[i12]
            base5 = result + i12 * 16
            (tuplei,tuplei6,) = e
            ptr7, len8 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base5, 4, len8)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base5, 0, ptr7)
            ptr9, len10 = _encode_utf8(tuplei6, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base5, 12, len10)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base5, 8, ptr9)
        ret = self.component.lift_callee79(caller, ptr, len2, variant, result, len11)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[int, Error]
        if load == 0:
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load13 & 0xffffffff)
        elif load == 1:
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load15 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr21 = load14
            len22 = load15
            result23: List[str] = []
            for i24 in range(0, len22):
                base16 = ptr21 + i24 * 8
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 0)
                load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, base16, 4)
                ptr19 = load17
                len20 = load18
                list = _decode_utf8(self.component._core_memory0, caller, ptr19, len20)
                result23.append(list)
            expected = Err(core.Error(result23))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def add_raw_auth(self, caller: wasmtime.Store, data: str) -> Result[int, Error]:
        ptr, len0 = _encode_utf8(data, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee80(caller, ptr, len0)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[int, Error]
        if load == 0:
            load1 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            expected = Ok(load1 & 0xffffffff)
        elif load == 1:
            load2 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr9 = load2
            len10 = load3
            result: List[str] = []
            for i11 in range(0, len10):
                base4 = ptr9 + i11 * 8
                load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 0)
                load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, base4, 4)
                ptr7 = load5
                len8 = load6
                list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
                result.append(list)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    def oauth2(self, caller: wasmtime.Store, service_name: str, scopes: str) -> Result[str, Error]:
        ptr, len0 = _encode_utf8(service_name, self.component._realloc0, self.component._core_memory0, caller)
        ptr1, len2 = _encode_utf8(scopes, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee81(caller, ptr, len0, ptr1, len2)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr5 = load3
            len6 = load4
            list = _decode_utf8(self.component._core_memory0, caller, ptr5, len6)
            expected = Ok(list)
        elif load == 1:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load7
            len16 = load8
            result: List[str] = []
            for i17 in range(0, len16):
                base9 = ptr15 + i17 * 8
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 0)
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 4)
                ptr12 = load10
                len13 = load11
                list14 = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
                result.append(list14)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def oauth2_without_profiler(self, caller: wasmtime.Store, service_name: str, scopes: str) -> Result[str, Error]:
        ptr, len0 = _encode_utf8(service_name, self.component._realloc0, self.component._core_memory0, caller)
        ptr1, len2 = _encode_utf8(scopes, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee82(caller, ptr, len0, ptr1, len2)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr5 = load3
            len6 = load4
            list = _decode_utf8(self.component._core_memory0, caller, ptr5, len6)
            expected = Ok(list)
        elif load == 1:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load7
            len16 = load8
            result: List[str] = []
            for i17 in range(0, len16):
                base9 = ptr15 + i17 * 8
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 0)
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 4)
                ptr12 = load10
                len13 = load11
                list14 = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
                result.append(list14)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def oauth2_with_extended_profiler(self, caller: wasmtime.Store, service_name: str, scopes: str, extension: str) -> Result[str, Error]:
        ptr, len0 = _encode_utf8(service_name, self.component._realloc0, self.component._core_memory0, caller)
        ptr1, len2 = _encode_utf8(scopes, self.component._realloc0, self.component._core_memory0, caller)
        ptr3, len4 = _encode_utf8(extension, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee83(caller, ptr, len0, ptr1, len2, ptr3, len4)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load6 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr7 = load5
            len8 = load6
            list = _decode_utf8(self.component._core_memory0, caller, ptr7, len8)
            expected = Ok(list)
        elif load == 1:
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr17 = load9
            len18 = load10
            result: List[str] = []
            for i19 in range(0, len18):
                base11 = ptr17 + i19 * 8
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 0)
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base11, 4)
                ptr14 = load12
                len15 = load13
                list16 = _decode_utf8(self.component._core_memory0, caller, ptr14, len15)
                result.append(list16)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def oauth2_with_custom_profiler(self, caller: wasmtime.Store, service_name: str, scopes: str, profiler: TypeId) -> Result[str, Error]:
        ptr, len0 = _encode_utf8(service_name, self.component._realloc0, self.component._core_memory0, caller)
        ptr1, len2 = _encode_utf8(scopes, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee84(caller, ptr, len0, ptr1, len2, _clamp(profiler, 0, 4294967295))
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load3 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr5 = load3
            len6 = load4
            list = _decode_utf8(self.component._core_memory0, caller, ptr5, len6)
            expected = Ok(list)
        elif load == 1:
            load7 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load7
            len16 = load8
            result: List[str] = []
            for i17 in range(0, len16):
                base9 = ptr15 + i17 * 8
                load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 0)
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base9, 4)
                ptr12 = load10
                len13 = load11
                list14 = _decode_utf8(self.component._core_memory0, caller, ptr12, len13)
                result.append(list14)
            expected = Err(core.Error(result))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def gql_deploy_query(self, caller: wasmtime.Store, params: QueryDeployParams) -> Result[str, Error]:
        record = params
        field = record.tg
        field0 = record.secrets
        ptr, len1 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        if field0 is None:
            variant = 0
            variant11 = 0
            variant12 = 0
        else:
            payload2 = field0
            vec = payload2
            len9 = len(vec)
            result = self.component._realloc0(caller, 0, 0, 4, len9 * 16)
            assert(isinstance(result, int))
            for i10 in range(0, len9):
                e = vec[i10]
                base3 = result + i10 * 16
                (tuplei,tuplei4,) = e
                ptr5, len6 = _encode_utf8(tuplei, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 4, len6)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 0, ptr5)
                ptr7, len8 = _encode_utf8(tuplei4, self.component._realloc0, self.component._core_memory0, caller)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 12, len8)
                _store(ctypes.c_uint32, self.component._core_memory0, caller, base3, 8, ptr7)
            variant = 1
            variant11 = result
            variant12 = len9
        ret = self.component.lift_callee85(caller, ptr, len1, variant, variant11, variant12)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr15 = load13
            len16 = load14
            list = _decode_utf8(self.component._core_memory0, caller, ptr15, len16)
            expected = Ok(list)
        elif load == 1:
            load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr25 = load17
            len26 = load18
            result27: List[str] = []
            for i28 in range(0, len26):
                base19 = ptr25 + i28 * 8
                load20 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 0)
                load21 = _load(ctypes.c_int32, self.component._core_memory0, caller, base19, 4)
                ptr22 = load20
                len23 = load21
                list24 = _decode_utf8(self.component._core_memory0, caller, ptr22, len23)
                result27.append(list24)
            expected = Err(core.Error(result27))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def gql_remove_query(self, caller: wasmtime.Store, tg_name: List[str]) -> Result[str, Error]:
        vec = tg_name
        len2 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len2 * 8)
        assert(isinstance(result, int))
        for i3 in range(0, len2):
            e = vec[i3]
            base0 = result + i3 * 8
            ptr, len1 = _encode_utf8(e, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, len1)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 0, ptr)
        ret = self.component.lift_callee86(caller, result, len2)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[str, Error]
        if load == 0:
            load4 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load5 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr6 = load4
            len7 = load5
            list = _decode_utf8(self.component._core_memory0, caller, ptr6, len7)
            expected = Ok(list)
        elif load == 1:
            load8 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load9 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr16 = load8
            len17 = load9
            result18: List[str] = []
            for i19 in range(0, len17):
                base10 = ptr16 + i19 * 8
                load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 0)
                load12 = _load(ctypes.c_int32, self.component._core_memory0, caller, base10, 4)
                ptr13 = load11
                len14 = load12
                list15 = _decode_utf8(self.component._core_memory0, caller, ptr13, len14)
                result18.append(list15)
            expected = Err(core.Error(result18))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return2(caller, ret)
        return expected
    def metagen_exec(self, caller: wasmtime.Store, config: FdkConfig) -> Result[List[FdkOutput], Error]:
        record = config
        field = record.workspace_path
        field0 = record.target_name
        field1 = record.config_json
        field2 = record.tg_json
        ptr, len3 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
        ptr4, len5 = _encode_utf8(field0, self.component._realloc0, self.component._core_memory0, caller)
        ptr6, len7 = _encode_utf8(field1, self.component._realloc0, self.component._core_memory0, caller)
        ptr8, len9 = _encode_utf8(field2, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee87(caller, ptr, len3, ptr4, len5, ptr6, len7, ptr8, len9)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[List[FdkOutput], Error]
        if load == 0:
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr23 = load10
            len24 = load11
            result: List[FdkOutput] = []
            for i25 in range(0, len24):
                base12 = ptr23 + i25 * 20
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 0)
                load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 4)
                ptr15 = load13
                len16 = load14
                list = _decode_utf8(self.component._core_memory0, caller, ptr15, len16)
                load17 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 8)
                load18 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 12)
                ptr19 = load17
                len20 = load18
                list21 = _decode_utf8(self.component._core_memory0, caller, ptr19, len20)
                load22 = _load(ctypes.c_uint8, self.component._core_memory0, caller, base12, 16)
                operand = load22
                if operand == 0:
                    boolean = False
                elif operand == 1:
                    boolean = True
                else:
                    raise TypeError("invalid variant discriminant for bool")
                result.append(FdkOutput(list, list21, boolean))
            expected = Ok(result)
        elif load == 1:
            load26 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load27 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr34 = load26
            len35 = load27
            result36: List[str] = []
            for i37 in range(0, len35):
                base28 = ptr34 + i37 * 8
                load29 = _load(ctypes.c_int32, self.component._core_memory0, caller, base28, 0)
                load30 = _load(ctypes.c_int32, self.component._core_memory0, caller, base28, 4)
                ptr31 = load29
                len32 = load30
                list33 = _decode_utf8(self.component._core_memory0, caller, ptr31, len32)
                result36.append(list33)
            expected = Err(core.Error(result36))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return5(caller, ret)
        return expected
    def metagen_write_files(self, caller: wasmtime.Store, items: List[FdkOutput], typegraph_dir: str) -> Result[None, Error]:
        vec = items
        len6 = len(vec)
        result = self.component._realloc0(caller, 0, 0, 4, len6 * 20)
        assert(isinstance(result, int))
        for i7 in range(0, len6):
            e = vec[i7]
            base0 = result + i7 * 20
            record = e
            field = record.path
            field1 = record.content
            field2 = record.overwrite
            ptr, len3 = _encode_utf8(field, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 4, len3)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 0, ptr)
            ptr4, len5 = _encode_utf8(field1, self.component._realloc0, self.component._core_memory0, caller)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 12, len5)
            _store(ctypes.c_uint32, self.component._core_memory0, caller, base0, 8, ptr4)
            _store(ctypes.c_uint8, self.component._core_memory0, caller, base0, 16, int(field2))
        ptr8, len9 = _encode_utf8(typegraph_dir, self.component._realloc0, self.component._core_memory0, caller)
        ret = self.component.lift_callee88(caller, result, len6, ptr8, len9)
        assert(isinstance(ret, int))
        load = _load(ctypes.c_uint8, self.component._core_memory0, caller, ret, 0)
        expected: Result[None, Error]
        if load == 0:
            expected = Ok(None)
        elif load == 1:
            load10 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 4)
            load11 = _load(ctypes.c_int32, self.component._core_memory0, caller, ret, 8)
            ptr17 = load10
            len18 = load11
            result19: List[str] = []
            for i20 in range(0, len18):
                base12 = ptr17 + i20 * 8
                load13 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 0)
                load14 = _load(ctypes.c_int32, self.component._core_memory0, caller, base12, 4)
                ptr15 = load13
                len16 = load14
                list = _decode_utf8(self.component._core_memory0, caller, ptr15, len16)
                result19.append(list)
            expected = Err(core.Error(result19))
        else:
            raise TypeError("invalid variant discriminant for expected")
        self.component._post_return0(caller, ret)
        return expected
    