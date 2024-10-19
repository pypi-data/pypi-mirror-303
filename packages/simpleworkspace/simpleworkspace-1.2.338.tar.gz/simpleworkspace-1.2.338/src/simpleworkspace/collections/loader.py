from simpleworkspace.__lazyimporter__ import __LazyImporter__, __TYPE_CHECKING__
if(__TYPE_CHECKING__):
    from . import observables as _observables
    from . import caseinsensitivedict as _caseinsensitivedict
observables: '_observables' = __LazyImporter__(__package__, '.observables')
caseinsensitivedict: '_caseinsensitivedict' = __LazyImporter__(__package__, '.caseinsensitivedict')