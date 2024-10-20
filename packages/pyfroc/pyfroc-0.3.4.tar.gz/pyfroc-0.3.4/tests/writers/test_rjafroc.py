#!/usr/bin/env python
# coding: UTF-8


from pyfroc.coords import ScannerCoordinates
from pyfroc.keys import CaseKey
from pyfroc.signals import Lesion
from pyfroc.writers.rjafroc import CaseIDDB, LesionIDDB


def test_caseiddb():
    caseid_db = CaseIDDB(idx_start=1)

    casekey1 = CaseKey(patient_id="patient1",
                       study_date="20210101",
                       modality="CT",
                       se_num="100")

    casekey2 = CaseKey(patient_id="patient2",
                       study_date="20210202",
                       modality="CT",
                       se_num="100")

    assert 1 == caseid_db.get_id(casekey1)

    # Return same id for same key
    assert 1 == caseid_db.get_id(casekey1)

    assert 2 == caseid_db.get_id(casekey2)


def test_lesioniddb():
    lesionid_db = LesionIDDB(idx_start=1)

    casekey1 = CaseKey(patient_id="patient1",
                       study_date="20210101",
                       modality="CT",
                       se_num="100")

    casekey2 = CaseKey(patient_id="patient2",
                       study_date="20210202",
                       modality="CT",
                       se_num="100")

    lesion1 = Lesion(ScannerCoordinates(0.0, 0.0, 0.0),
                     r=1.0,
                     name="lesion1")

    lesion2 = Lesion(ScannerCoordinates(0.0, 0.0, 1.0),
                     r=1.0,
                     name="lesion2")

    assert 1 == lesionid_db.get_id(casekey1, lesion1)
    assert 2 == lesionid_db.get_id(casekey1, lesion2)

    # Return same id for same key
    assert 1 == lesionid_db.get_id(casekey1, lesion1)

    assert 1 == lesionid_db.get_id(casekey2, lesion1)
    assert 2 == lesionid_db.get_id(casekey2, lesion2)
