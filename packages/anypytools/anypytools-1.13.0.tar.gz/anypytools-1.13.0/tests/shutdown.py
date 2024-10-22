import anypytools
import anypytools.macro_commands as mc

macros = [
    [
        mc.Load(
            r"D:\AMMRs\ammr\Application\MocapExamples\Plug-in-gait_Simple\FullBody.main.any"
        ),
        mc.OperationRun("Main.RunAnalysis.LoadParameters"),
        mc.OperationRun("Main.Studies.InverseDynamics"),
    ]
] * 30

app = anypytools.AnyPyProcess(num_processes=3)

app.start_macro(macros)
