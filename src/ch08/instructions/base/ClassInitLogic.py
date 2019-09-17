class ClassInitLogic():

    @staticmethod
    def initClass(thread, clazz):
        clazz.start_init()
        ClassInitLogic.scheduleClinit(thread, clazz)
        ClassInitLogic.initSuperClass(thread, clazz)

    @staticmethod
    def scheduleClinit(thread, clazz):
       clinit = clazz.get_clinit_method()
       if clinit:
           newFrame = thread.newFrame(clinit)
           thread.push_frame(newFrame)

    @staticmethod
    def initSuperClass(thread, clazz):
        if not clazz.is_interface():
            superClass = clazz.superClass
            if superClass and not superClass.initStarted:
                ClassInitLogic.initClass(thread, superClass)
