from setuptools import setup

long_description = """
# QuantConnect Stubs

This package contains type stubs for QuantConnect's [Lean](https://github.com/QuantConnect/Lean) algorithmic trading engine and for parts of the .NET library that are used by Lean.

These stubs can be used by editors to provide type-aware features like autocomplete and auto-imports in QuantConnect strategies written in Python.

After installing the stubs, you can copy the following line to the top of every Python file to have the same imports as the ones that are added by default in the cloud:
```py
from AlgorithmImports import *
```

This line imports [all common QuantConnect members](https://github.com/QuantConnect/Lean/blob/master/Common/AlgorithmImports.py) and provides autocomplete for them.
""".strip()

setup(
    name="quantconnect-stubs",
    version="16694",
    description="Type stubs for QuantConnect's Lean",
    author="QuantConnect",
    author_email="support@quantconnect.com",
    url="https://github.com/QuantConnect/quantconnect-stubs-generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3"
    ],
    install_requires=["pandas", "matplotlib"],
    packages=[
        "AlgorithmImports",
        "clr",
        "exports",
        "Internal",
        "Internal.Runtime",
        "Internal.Runtime.CompilerHelpers",
        "Internal.Runtime.InteropServices",
        "Internal.Win32",
        "Internal.Win32.SafeHandles",
        "Microsoft",
        "Microsoft.Win32",
        "Microsoft.Win32.SafeHandles",
        "MS",
        "MS.Internal",
        "MS.Internal.Xml",
        "MS.Internal.Xml.Linq",
        "MS.Internal.Xml.Linq.ComponentModel",
        "QuantConnect",
        "QuantConnect.Algorithm",
        "QuantConnect.Algorithm.Framework",
        "QuantConnect.Algorithm.Framework.Alphas",
        "QuantConnect.Algorithm.Framework.Alphas.Analysis",
        "QuantConnect.Algorithm.Framework.Alphas.Serialization",
        "QuantConnect.Algorithm.Framework.Execution",
        "QuantConnect.Algorithm.Framework.Portfolio",
        "QuantConnect.Algorithm.Framework.Portfolio.SignalExports",
        "QuantConnect.Algorithm.Framework.Risk",
        "QuantConnect.Algorithm.Framework.Selection",
        "QuantConnect.Algorithm.Selection",
        "QuantConnect.AlgorithmFactory",
        "QuantConnect.AlgorithmFactory.Python",
        "QuantConnect.AlgorithmFactory.Python.Wrappers",
        "QuantConnect.Api",
        "QuantConnect.Api.Serialization",
        "QuantConnect.Benchmarks",
        "QuantConnect.Brokerages",
        "QuantConnect.Brokerages.Backtesting",
        "QuantConnect.Brokerages.CrossZero",
        "QuantConnect.Brokerages.Paper",
        "QuantConnect.Commands",
        "QuantConnect.Configuration",
        "QuantConnect.Data",
        "QuantConnect.Data.Auxiliary",
        "QuantConnect.Data.Common",
        "QuantConnect.Data.Consolidators",
        "QuantConnect.Data.Custom",
        "QuantConnect.Data.Custom.AlphaStreams",
        "QuantConnect.Data.Custom.IconicTypes",
        "QuantConnect.Data.Custom.Intrinio",
        "QuantConnect.Data.Custom.Tiingo",
        "QuantConnect.Data.Fundamental",
        "QuantConnect.Data.Market",
        "QuantConnect.Data.Shortable",
        "QuantConnect.Data.UniverseSelection",
        "QuantConnect.DataSource",
        "QuantConnect.DownloaderDataProvider",
        "QuantConnect.DownloaderDataProvider.Launcher",
        "QuantConnect.DownloaderDataProvider.Launcher.Models",
        "QuantConnect.DownloaderDataProvider.Launcher.Models.Constants",
        "QuantConnect.Exceptions",
        "QuantConnect.Indicators",
        "QuantConnect.Indicators.CandlestickPatterns",
        "QuantConnect.Interfaces",
        "QuantConnect.Lean",
        "QuantConnect.Lean.Engine",
        "QuantConnect.Lean.Engine.DataFeeds",
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators",
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories",
        "QuantConnect.Lean.Engine.DataFeeds.Queues",
        "QuantConnect.Lean.Engine.DataFeeds.Transport",
        "QuantConnect.Lean.Engine.DataFeeds.WorkScheduling",
        "QuantConnect.Lean.Engine.HistoricalData",
        "QuantConnect.Lean.Engine.RealTime",
        "QuantConnect.Lean.Engine.Results",
        "QuantConnect.Lean.Engine.Server",
        "QuantConnect.Lean.Engine.Setup",
        "QuantConnect.Lean.Engine.Storage",
        "QuantConnect.Lean.Engine.TransactionHandlers",
        "QuantConnect.Lean.Launcher",
        "QuantConnect.Logging",
        "QuantConnect.Messaging",
        "QuantConnect.Notifications",
        "QuantConnect.Optimizer",
        "QuantConnect.Optimizer.Launcher",
        "QuantConnect.Optimizer.Objectives",
        "QuantConnect.Optimizer.Parameters",
        "QuantConnect.Optimizer.Strategies",
        "QuantConnect.Orders",
        "QuantConnect.Orders.Fees",
        "QuantConnect.Orders.Fills",
        "QuantConnect.Orders.OptionExercise",
        "QuantConnect.Orders.Serialization",
        "QuantConnect.Orders.Slippage",
        "QuantConnect.Orders.TimeInForces",
        "QuantConnect.Packets",
        "QuantConnect.Parameters",
        "QuantConnect.Python",
        "QuantConnect.Queues",
        "QuantConnect.Report",
        "QuantConnect.Report.ReportElements",
        "QuantConnect.Research",
        "QuantConnect.Scheduling",
        "QuantConnect.Securities",
        "QuantConnect.Securities.Cfd",
        "QuantConnect.Securities.Crypto",
        "QuantConnect.Securities.CryptoFuture",
        "QuantConnect.Securities.CurrencyConversion",
        "QuantConnect.Securities.Equity",
        "QuantConnect.Securities.Forex",
        "QuantConnect.Securities.Future",
        "QuantConnect.Securities.FutureOption",
        "QuantConnect.Securities.FutureOption.Api",
        "QuantConnect.Securities.Index",
        "QuantConnect.Securities.IndexOption",
        "QuantConnect.Securities.Interfaces",
        "QuantConnect.Securities.Option",
        "QuantConnect.Securities.Option.StrategyMatcher",
        "QuantConnect.Securities.Positions",
        "QuantConnect.Securities.Volatility",
        "QuantConnect.Statistics",
        "QuantConnect.Storage",
        "QuantConnect.Util",
        "QuantConnect.Util.RateLimit",
        "System",
        "System.Buffers",
        "System.Buffers.Binary",
        "System.Buffers.Text",
        "System.CodeDom",
        "System.CodeDom.Compiler",
        "System.Collections",
        "System.Collections.Concurrent",
        "System.Collections.Frozen",
        "System.Collections.Generic",
        "System.Collections.Immutable",
        "System.Collections.ObjectModel",
        "System.Collections.Specialized",
        "System.ComponentModel",
        "System.ComponentModel.DataAnnotations",
        "System.ComponentModel.DataAnnotations.Schema",
        "System.ComponentModel.Design",
        "System.ComponentModel.Design.Serialization",
        "System.Configuration",
        "System.Configuration.Assemblies",
        "System.Diagnostics",
        "System.Diagnostics.CodeAnalysis",
        "System.Diagnostics.Contracts",
        "System.Diagnostics.SymbolStore",
        "System.Diagnostics.Tracing",
        "System.Drawing",
        "System.Globalization",
        "System.IO",
        "System.IO.Enumeration",
        "System.IO.Strategies",
        "System.Linq",
        "System.Net",
        "System.Net.Cache",
        "System.Net.NetworkInformation",
        "System.Net.Security",
        "System.Net.Sockets",
        "System.Numerics",
        "System.Numerics.Hashing",
        "System.Reflection",
        "System.Reflection.Emit",
        "System.Reflection.Metadata",
        "System.Resources",
        "System.Runtime",
        "System.Runtime.CompilerServices",
        "System.Runtime.ConstrainedExecution",
        "System.Runtime.ExceptionServices",
        "System.Runtime.InteropServices",
        "System.Runtime.InteropServices.ComTypes",
        "System.Runtime.InteropServices.Marshalling",
        "System.Runtime.InteropServices.ObjectiveC",
        "System.Runtime.InteropServices.Swift",
        "System.Runtime.Intrinsics",
        "System.Runtime.Intrinsics.Arm",
        "System.Runtime.Intrinsics.Wasm",
        "System.Runtime.Intrinsics.X86",
        "System.Runtime.Loader",
        "System.Runtime.Remoting",
        "System.Runtime.Serialization",
        "System.Runtime.Versioning",
        "System.Security",
        "System.Security.Authentication",
        "System.Security.Authentication.ExtendedProtection",
        "System.Security.Cryptography",
        "System.Security.Permissions",
        "System.Security.Principal",
        "System.Text",
        "System.Text.RegularExpressions",
        "System.Text.RegularExpressions.Symbolic",
        "System.Text.Unicode",
        "System.Threading",
        "System.Threading.Tasks",
        "System.Threading.Tasks.Sources",
        "System.Timers",
        "System.Windows",
        "System.Windows.Input",
        "System.Windows.Markup",
        "WasiPollWorld",
        "WasiPollWorld.wit",
        "WasiPollWorld.wit.imports",
        "WasiPollWorld.wit.imports.wasi",
        "WasiPollWorld.wit.imports.wasi.clocks",
        "WasiPollWorld.wit.imports.wasi.clocks.v0_2_0",
        "WasiPollWorld.wit.imports.wasi.io",
        "WasiPollWorld.wit.imports.wasi.io.v0_2_0"
    ],
    package_data={
        "AlgorithmImports": ["*.py", "*.pyi", "py.typed"],
        "clr": ["*.py", "*.pyi", "py.typed"],
        "exports": ["*.py", "*.pyi", "py.typed"],
        "Internal": ["*.py", "*.pyi", "py.typed"],
        "Internal.Runtime": ["*.py", "*.pyi", "py.typed"],
        "Internal.Runtime.CompilerHelpers": ["*.py", "*.pyi", "py.typed"],
        "Internal.Runtime.InteropServices": ["*.py", "*.pyi", "py.typed"],
        "Internal.Win32": ["*.py", "*.pyi", "py.typed"],
        "Internal.Win32.SafeHandles": ["*.py", "*.pyi", "py.typed"],
        "Microsoft": ["*.py", "*.pyi", "py.typed"],
        "Microsoft.Win32": ["*.py", "*.pyi", "py.typed"],
        "Microsoft.Win32.SafeHandles": ["*.py", "*.pyi", "py.typed"],
        "MS": ["*.py", "*.pyi", "py.typed"],
        "MS.Internal": ["*.py", "*.pyi", "py.typed"],
        "MS.Internal.Xml": ["*.py", "*.pyi", "py.typed"],
        "MS.Internal.Xml.Linq": ["*.py", "*.pyi", "py.typed"],
        "MS.Internal.Xml.Linq.ComponentModel": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Alphas": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Alphas.Analysis": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Alphas.Serialization": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Execution": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Portfolio": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Portfolio.SignalExports": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Risk": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Framework.Selection": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Algorithm.Selection": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.AlgorithmFactory": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.AlgorithmFactory.Python": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.AlgorithmFactory.Python.Wrappers": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Api": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Api.Serialization": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Benchmarks": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Brokerages": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Brokerages.Backtesting": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Brokerages.CrossZero": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Brokerages.Paper": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Commands": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Configuration": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Auxiliary": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Common": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Consolidators": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Custom": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Custom.AlphaStreams": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Custom.IconicTypes": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Custom.Intrinio": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Custom.Tiingo": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Fundamental": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Market": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.Shortable": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Data.UniverseSelection": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.DataSource": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.DownloaderDataProvider": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.DownloaderDataProvider.Launcher": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.DownloaderDataProvider.Launcher.Models": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.DownloaderDataProvider.Launcher.Models.Constants": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Exceptions": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Indicators": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Indicators.CandlestickPatterns": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Interfaces": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds.Queues": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds.Transport": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.DataFeeds.WorkScheduling": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.HistoricalData": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.RealTime": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.Results": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.Server": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.Setup": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.Storage": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Engine.TransactionHandlers": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Lean.Launcher": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Logging": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Messaging": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Notifications": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Optimizer": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Optimizer.Launcher": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Optimizer.Objectives": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Optimizer.Parameters": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Optimizer.Strategies": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.Fees": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.Fills": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.OptionExercise": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.Serialization": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.Slippage": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Orders.TimeInForces": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Packets": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Parameters": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Python": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Queues": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Report": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Report.ReportElements": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Research": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Scheduling": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Cfd": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Crypto": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.CryptoFuture": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.CurrencyConversion": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Equity": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Forex": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Future": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.FutureOption": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.FutureOption.Api": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Index": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.IndexOption": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Interfaces": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Option": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Option.StrategyMatcher": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Positions": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Securities.Volatility": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Statistics": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Storage": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Util": ["*.py", "*.pyi", "py.typed"],
        "QuantConnect.Util.RateLimit": ["*.py", "*.pyi", "py.typed"],
        "System": ["*.py", "*.pyi", "py.typed"],
        "System.Buffers": ["*.py", "*.pyi", "py.typed"],
        "System.Buffers.Binary": ["*.py", "*.pyi", "py.typed"],
        "System.Buffers.Text": ["*.py", "*.pyi", "py.typed"],
        "System.CodeDom": ["*.py", "*.pyi", "py.typed"],
        "System.CodeDom.Compiler": ["*.py", "*.pyi", "py.typed"],
        "System.Collections": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.Concurrent": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.Frozen": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.Generic": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.Immutable": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.ObjectModel": ["*.py", "*.pyi", "py.typed"],
        "System.Collections.Specialized": ["*.py", "*.pyi", "py.typed"],
        "System.ComponentModel": ["*.py", "*.pyi", "py.typed"],
        "System.ComponentModel.DataAnnotations": ["*.py", "*.pyi", "py.typed"],
        "System.ComponentModel.DataAnnotations.Schema": ["*.py", "*.pyi", "py.typed"],
        "System.ComponentModel.Design": ["*.py", "*.pyi", "py.typed"],
        "System.ComponentModel.Design.Serialization": ["*.py", "*.pyi", "py.typed"],
        "System.Configuration": ["*.py", "*.pyi", "py.typed"],
        "System.Configuration.Assemblies": ["*.py", "*.pyi", "py.typed"],
        "System.Diagnostics": ["*.py", "*.pyi", "py.typed"],
        "System.Diagnostics.CodeAnalysis": ["*.py", "*.pyi", "py.typed"],
        "System.Diagnostics.Contracts": ["*.py", "*.pyi", "py.typed"],
        "System.Diagnostics.SymbolStore": ["*.py", "*.pyi", "py.typed"],
        "System.Diagnostics.Tracing": ["*.py", "*.pyi", "py.typed"],
        "System.Drawing": ["*.py", "*.pyi", "py.typed"],
        "System.Globalization": ["*.py", "*.pyi", "py.typed"],
        "System.IO": ["*.py", "*.pyi", "py.typed"],
        "System.IO.Enumeration": ["*.py", "*.pyi", "py.typed"],
        "System.IO.Strategies": ["*.py", "*.pyi", "py.typed"],
        "System.Linq": ["*.py", "*.pyi", "py.typed"],
        "System.Net": ["*.py", "*.pyi", "py.typed"],
        "System.Net.Cache": ["*.py", "*.pyi", "py.typed"],
        "System.Net.NetworkInformation": ["*.py", "*.pyi", "py.typed"],
        "System.Net.Security": ["*.py", "*.pyi", "py.typed"],
        "System.Net.Sockets": ["*.py", "*.pyi", "py.typed"],
        "System.Numerics": ["*.py", "*.pyi", "py.typed"],
        "System.Numerics.Hashing": ["*.py", "*.pyi", "py.typed"],
        "System.Reflection": ["*.py", "*.pyi", "py.typed"],
        "System.Reflection.Emit": ["*.py", "*.pyi", "py.typed"],
        "System.Reflection.Metadata": ["*.py", "*.pyi", "py.typed"],
        "System.Resources": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.CompilerServices": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.ConstrainedExecution": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.ExceptionServices": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.InteropServices": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.InteropServices.ComTypes": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.InteropServices.Marshalling": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.InteropServices.ObjectiveC": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.InteropServices.Swift": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Intrinsics": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Intrinsics.Arm": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Intrinsics.Wasm": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Intrinsics.X86": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Loader": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Remoting": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Serialization": ["*.py", "*.pyi", "py.typed"],
        "System.Runtime.Versioning": ["*.py", "*.pyi", "py.typed"],
        "System.Security": ["*.py", "*.pyi", "py.typed"],
        "System.Security.Authentication": ["*.py", "*.pyi", "py.typed"],
        "System.Security.Authentication.ExtendedProtection": ["*.py", "*.pyi", "py.typed"],
        "System.Security.Cryptography": ["*.py", "*.pyi", "py.typed"],
        "System.Security.Permissions": ["*.py", "*.pyi", "py.typed"],
        "System.Security.Principal": ["*.py", "*.pyi", "py.typed"],
        "System.Text": ["*.py", "*.pyi", "py.typed"],
        "System.Text.RegularExpressions": ["*.py", "*.pyi", "py.typed"],
        "System.Text.RegularExpressions.Symbolic": ["*.py", "*.pyi", "py.typed"],
        "System.Text.Unicode": ["*.py", "*.pyi", "py.typed"],
        "System.Threading": ["*.py", "*.pyi", "py.typed"],
        "System.Threading.Tasks": ["*.py", "*.pyi", "py.typed"],
        "System.Threading.Tasks.Sources": ["*.py", "*.pyi", "py.typed"],
        "System.Timers": ["*.py", "*.pyi", "py.typed"],
        "System.Windows": ["*.py", "*.pyi", "py.typed"],
        "System.Windows.Input": ["*.py", "*.pyi", "py.typed"],
        "System.Windows.Markup": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports.wasi": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports.wasi.clocks": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports.wasi.clocks.v0_2_0": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports.wasi.io": ["*.py", "*.pyi", "py.typed"],
        "WasiPollWorld.wit.imports.wasi.io.v0_2_0": ["*.py", "*.pyi", "py.typed"]
    }
)
