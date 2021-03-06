#!/usr/bin/python

import SARpy
import operator
f1 =SARpy.Filter('CLASS','Low',operator.eq)
f2 =SARpy.Filter('CLASS','Moderate',operator.eq)
f3 =SARpy.Filter('CLASS','Strong',operator.eq)
f4 =SARpy.Filter('CLASS','Extreme',operator.eq)
filt = SARpy.Filter('ID','200',operator.lt)
dict = {'INACTIVE':f1,'INACTIVE':f2,'ACTIVE':f3,'ACTIVE':f4}
dataset =  SARpy.loadDataset("ds.csv", "csv", dict, "SMILES")
SARpy.fragmentize(dataset,2,18)
rules = SARpy.extract(dataset, 3,1,None)
SARpy.saveSmarts(rules, "ruleset.txt")
pred = SARpy.predict(rules, dataset)
SARpy.savePredictions(dataset, "prediction.txt")
SARpy.validate(dataset)
