============================= test session starts ==============================
platform linux -- Python 3.10.13, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/ltruciosr/Documents/programming/tenpo/mlops
plugins: anyio-3.7.1
collected 0 items

============================ no tests ran in 0.00s =============================
============================= test session starts ==============================
platform linux -- Python 3.10.13, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/ltruciosr/Documents/programming/tenpo/mlops
plugins: anyio-3.7.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____________________ ERROR collecting tests/test_model.py _____________________
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/runner.py:341: in from_call
    result: Optional[TResult] = func()
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/runner.py:372: in <lambda>
    call = CallInfo.from_call(lambda: list(collector.collect()), "collect")
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/python.py:531: in collect
    self._inject_setup_module_fixture()
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/python.py:545: in _inject_setup_module_fixture
    self.obj, ("setUpModule", "setup_module")
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/python.py:310: in obj
    self._obj = obj = self._getobj()
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/python.py:528: in _getobj
    return self._importtestmodule()
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/python.py:617: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/pathlib.py:567: in import_path
    importlib.import_module(module_name)
../../../../miniconda3/envs/ml/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1050: in _gcd_import
    ???
<frozen importlib._bootstrap>:1027: in _find_and_load
    ???
<frozen importlib._bootstrap>:1006: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:688: in _load_unlocked
    ???
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/_pytest/assertion/rewrite.py:186: in exec_module
    exec(co, module.__dict__)
tests/test_model.py:5: in <module>
    MODEL = torch.jit.load(MODEL_PATH, map_location=DEVICE)
../../../../miniconda3/envs/ml/lib/python3.10/site-packages/torch/jit/_serialization.py:152: in load
    raise ValueError(f"The provided filename {f} does not exist")  # type: ignore[str-bytes-safe]
E   ValueError: The provided filename /models/doubleit_model.pt does not exist
=========================== short test summary info ============================
ERROR tests/test_model.py - ValueError: The provided filename /models/doublei...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 1.54s ===============================
