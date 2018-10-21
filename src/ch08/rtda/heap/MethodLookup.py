class MethodLookup():

    @staticmethod
    def lookupMethodInClass(clazz, name, descriptor):
        c = clazz
        while c:
            for method in c.methods:
                if method.name == name and method.descriptor == descriptor:
                    return method
            c = c.superClass
        return None

    @staticmethod
    def lookupMethodInInterfaces(ifaces, name, descriptor):
        for iface in ifaces:
            for method in iface.methods:
                if method.name == name and method.descriptor == descriptor:
                    return method
            method = MethodLookup.lookupMethodInInterfaces(iface.interfaces, name, descriptor)
            if method:
                return method

        return None