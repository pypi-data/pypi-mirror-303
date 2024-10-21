from __future__ import annotations

import logging
import typing
from collections.abc import Mapping, Iterable
from typing import TypeVar, Generic, Callable, ParamSpec

import pandas as pd

from mdata.core.shared_defs import SpecType

RawSpec = TypeVar('RawSpec')
Spec = TypeVar('Spec')
Cont = TypeVar('Cont')
MD = TypeVar('MD')


class SpecFac(Generic[RawSpec, Spec]):
    constructors: dict[type, Callable[[SpecType, RawSpec], Spec]]

    def __init__(self, spec_cls: type[Spec] = None) -> None:
        spec_cls = typing.get_args(self.__class__)[1] if spec_cls is None else spec_cls
        self.constr = self.constructors[spec_cls]
        self.__call__ = self.make

    def make(self, typ: SpecType, base_spec: RawSpec) -> Spec:
        return self.constr(typ, base_spec)


class ContFac(Generic[Spec, Cont]):
    constructors: dict[Cont, Callable[[Spec, pd.DataFrame], Cont]]

    def __init__(self, cont_cls: type[Cont]):
        cont_cls = typing.get_args(self.__class__)[1] if cont_cls is None else cont_cls
        self.constr = self.constructors[cont_cls]
        self.__call__ = self.make

    def make(self, s_spec: Spec, df: pd.DataFrame) -> Cont:
        return self.constr(s_spec, df)

class CombContFac(ContFac[Spec, Cont]):
    constructors: dict[Cont, Callable[[Iterable[Spec], pd.DataFrame], Cont]]

    def make(self, s_specs: Iterable[Spec], df: pd.DataFrame) -> Cont:
        return self.constr(s_specs, df)

class MDFac(Generic[MD]):
    constructors: dict[type[MD], Callable[[...], MD]]

    def __init__(self, md_cls: type[MD]) -> None:
        md_cls = typing.get_args(self.__class__)[0] if md_cls is None else md_cls
        self.constr = self.constructors[md_cls]
        self.__call__ = self.make

    def make(self, **kwargs) -> MD:
        constr = self.constr(**kwargs)
        if not (constr.supported_extensions >= constr.meta.extensions):
            logging.warning(
                f'MachineData type does not support all listed extensions in metadata: {constr.supported_extensions} >!= {constr.meta.extensions}')
        return constr

def spec_fac_for_cls(fac_cls: type[SpecFac[RawSpec, Spec]], raw_spec_cls: type[RawSpec], spec_cls: type[Spec],
                     **kwargs) -> SpecFac[RawSpec, Spec]:
    return typing.cast(SpecFac[RawSpec, Spec], fac_cls[spec_cls](spec_cls, **kwargs))


def cont_fac_for_cls(fac_cls: type[ContFac[Spec, Cont]], spec_cls: type[Spec], cont_cls: type[Cont], **kwargs) -> \
        ContFac[Spec, Cont]:
    return typing.cast(ContFac[Spec, Cont], fac_cls[spec_cls, cont_cls](cont_cls, **kwargs))

def comb_cont_fac_for_cls(fac_cls: type[ContFac[Spec, Cont]], spec_cls: type[Spec], cont_cls: type[Cont], **kwargs) -> \
        CombContFac[Spec, Cont]:
    return typing.cast(CombContFac[Spec, Cont], fac_cls[spec_cls, cont_cls](cont_cls, **kwargs))

def md_fac_for_cls(fac_cls: type[MDFac[MD]], md_cls: type[MD]) -> MDFac[MD]:
    return typing.cast(MDFac[MD], fac_cls[md_cls](md_cls))