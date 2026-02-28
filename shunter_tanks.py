import sys, CurrentVehicle
from gui.SystemMessages import pushMessage, SM_TYPE
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
msg = "clientside restrictions removed // " + "\xEE\xE3\xF0\xE0\xED\xE8\xF7\xE5\xED\xE8\xFF\x20\xF1\xEE\x20\xF1\xF2\xEE\xF0\xEE\xED\xFB\x20\xEA\xEB\xE8\xE5\xED\xF2\xE0\x20\xF3\xE4\xE0\xEB\xE5\xED\xFB".decode('cp1251')

pushMessage(msg, SM_TYPE.Warning)
