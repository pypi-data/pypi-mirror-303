import jpype
import jpype.imports  # This enables direct import of java classes
from typing import List, Union, Optional
# import jpype.beans  # This creates pythonic versions of getters / setters (as in JCC version)

import os

# Get the  path of the current file, used for finding the jars directory
dirpath = os.path.dirname(os.path.abspath(__file__))


def initVM(vmargs: Union[str, None] = None,
           additional_classpaths: Union[List, None] = None,
           jvmpath: Optional[Union[str, os.PathLike]] = None):
    """
    Initializes the Java Virtual Machine (JVM) for Orekit.

    Args:
        vmargs (Union[str, None], optional): Additional arguments to pass to the JVM. Defaults to None.
             Example for debugging: vmargs='-Xcheck:jni,-verbose:jni,-verbose:class,-XX:+UnlockDiagnosticVMOptions'
        additional_classpaths (Union[List, None], optional): Additional classpaths to add to the JVM. Defaults to None.
        jvmpath (Union[str, os.PathLike], optional): Path to the jvm library file,
            Typically one of (``libjvm.so``, ``jvm.dll``, ...)
            Defaults to None, in this case Jpype will look for a JDK on the system.

    Raises:
        FileNotFoundError: If any of the additional classpaths do not exist.

    """
    # Set the classpath
    if additional_classpaths is not None:
        for classpath in additional_classpaths:
            if not os.path.exists(classpath):
                raise FileNotFoundError(f"Classpath {os.path.abspath(classpath)} does not exist")
            jpype.addClassPath(os.path.abspath(classpath))

    # Add standard orekit jars to the classpath
    if not jpype.isJVMStarted():
        jpype.addClassPath(os.path.join(dirpath, 'jars', '*'))

        # Start the JVM
        # '-Xcheck:jni','-verbose:jni','-verbose:class'
        if vmargs is not None:
            jpype.startJVM(*vmargs.split(","), convertStrings=True, jvmpath=jvmpath)
        else:
            jpype.startJVM(convertStrings=True, jvmpath=jvmpath)
    else:
        print("JVM already started, resuming on started JVM")

    # Perform modifications for orekit
    import orekit_jpype.orekit_converters  # noqa: F401
