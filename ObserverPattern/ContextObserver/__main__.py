from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

"""In this changes context managers will be used to provide a way to ensuere that observers are
properly detached.

when accesing the subject and its observers, this way when an observer is done observing, it will detach itself
automatically, even if an exception is raised during processing, not only that, the subject take care  of cleaning up
any lefover observers when its context exits, as a consequence, there should be no more dangling references
 """


# Report on current KPI values
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

print ('\n***Exited context managers.***\n\n')
kpis.set_kpis(150, 110, 120)
