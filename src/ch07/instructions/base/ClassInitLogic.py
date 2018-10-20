class ClassInitLogic():

    @staticmethod
    def initClass(thread, clazz):
        clazz.startInit()
        ClassInitLogic.scheduleClinit(thread, clazz)
        ClassInitLogic.initSuperClass(thread, clazz)

    @staticmethod
    def scheduleClinit(thread, clazz):
       clinit = clazz.getClinitMethod()
       if clinit:
           newFrame = thread.newFrame(clinit)
           thread.pushFrame(newFrame)

    @staticmethod
    def initSuperClass(thread, clazz):
        if not clazz.isInterface():
            superClass = clazz.superClass
            if superClass and not superClass.initStarted:
                ClassInitLogic.initClass(thread, superClass)
