import sys, CurrentVehicle
from CurrentVehicle import _CurrentVehicle, g_currentVehicle
from gui.shared.gui_items.Vehicle import Vehicle

_CurrentVehicle.selectVehicle = lambda self, vID=0, cb=None, wait=False: self._selectVehicle(vID, cb, wait)
_CurrentVehicle._CurrentVehicle__selectNoVehicle = lambda self: None

try:
    from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
    PreQueuePermissions.canChangeVehicle = lambda self: True
    PreQueuePermissions.canCreateSquad = lambda self: True
except Exception as err: print "err: " + str(err)

try:
    from gui.prb_control.entities.base.actions_validator import CurrentVehicleActionsValidator
    CurrentVehicleActionsValidator._validate = lambda self: None
except Exception as err: print "err: " + str(err)

Vehicle.isReadyToFight = property(lambda self: True)
Vehicle.isReadyToPrebattle = lambda self: True
Vehicle.isUnsuitableToQueue = lambda self: False
Vehicle.getState = lambda self: ('ready', 0)
_CurrentVehicle.isUnsuitableToQueue = lambda self: False

g_currentVehicle.onChanged()
print "done"