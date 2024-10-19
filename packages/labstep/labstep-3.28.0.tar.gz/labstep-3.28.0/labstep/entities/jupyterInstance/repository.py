#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED
from labstep.entities.jupyterInstance.model import JupyterInstance


def getJupyterInstance(user, id):
    return entityRepository.getEntity(user, JupyterInstance, id)


def editJupyterInstance(
    jupyterInstance,
    startedAt=UNSPECIFIED,
    endedAt=UNSPECIFIED,
    status=UNSPECIFIED,
    errorMessage=UNSPECIFIED
):
    params = {
        "started_at": startedAt,
        "ended_at": endedAt,
        "status": status,
        "error_message": errorMessage,
    }

    return entityRepository.editEntity(jupyterInstance, params)
