---
title: "Python Recurcepton: The making of a program that traces recursion"
author: JC
layout: post
category: slog
---

Lately, we have been talking a lot about [recursion](https://en.wikipedia.org/wiki/Recursion) in class at U of T. Specifically, we have been asked to *trace* recursive functions in order to find their output. While this is fun on its own, I shall go to another level for the sake of keeping this blog interesting. I asked myself, why trace recursive functions when I can **make a function that traces recursive functions for me**? I call this *recurception*.

The code I came up with took me a fair amount of time, and makes use of the [sys](https://docs.python.org/3/library/sys.html) and [inspect](https://docs.python.org/3/library/inspect.html) built-in modules. The code goes like this:


    import sys
    import inspect
    
    def global_tracer(frame, event, arg):
        """ (frame, str, object) -> function
        
        Return a local tracer.
    
        """
        return local_tracer
    
    def local_tracer(frame, event, arg):
        """ (frame, str, object) -> function
        
        Trace a local event and return itself.
    
        """
        if(event == "return"):
            # Get function name
            result = frame.f_code.co_name
            if(not result.startswith("<") and result != "recurception"):
                # Get function arguments and values
                args, _, _, values = inspect.getargvalues(frame)
    
                # Build Result String
                result += "("
                arglist = ['"' + values[i] + '"' if isinstance(values[i], str) else repr(values[i]) for i in args]
                result += ", ".join(arglist)
                result += ") -> "
                result += '"' + arg + '"' if isinstance(arg, str) else repr(arg)
    
                # Print it
                print(result)
        return local_tracer
    
    def recurception(recursive, arguments):
        """ (function, list of arguments) -> NoneType
    
        Trace the recurssion of a recursive function.
    
        """
        sys.settrace(global_tracer)
        result = recursive(*arguments)

In order to use it, you must define a recursive function (or any other type of function really), such as the following, taken from a class assignment/lab:

    def nested_concat(L):
        """(list or str) -> str
    
        Return L if it’s a str, if L is a (possibly-nested) str return
        concatenation of str elements of L and (possibly-nested) sublists of L.
    
        Assume: Elements of L are either str or lists with elements that
        satisfy this same assumption.
    
        """
        if isinstance(L, str):
            return L
        else: # L is a possibly-nested list of str
            return "".join([nested_concat(x) for x in L])

And run it through the recurception like this

    >>> recurception(nested_concat, ["yes"])
    nested_concat("yes") -> "yes"
    >>> recurception(nested_concat, [[["yes", " it"], " works"]])
    nested_concat("yes") -> "yes"
    nested_concat(" it") -> " it"
    nested_concat(['yes', ' it']) -> "yes it"
    nested_concat(" works") -> " works"
    nested_concat([['yes', ' it'], ' works']) -> "yes it works"

The first argument of *recurception* is a function, and the second is a list of arguments to pass to such function. It takes care of printing each call to a function and its return value, such that all recursion steps are logged. I thought it was fairly interesting, and learned a lot about Python tracing and the built-in data types such as *frames* and (precompiled) *code*.

Keep being recursive,  
Juan Camilo Osorio