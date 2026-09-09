from conftest import CONTRACT
A='https://log-one.example/a';B='https://log-two.example/b';STEPS=['isolate equipment','inspect seal','restart service']
def seed(vm,v='IN_ORDER'):
 vm.mock_web(r'log-one\.example',{'status':200,'body':'isolate equipment then inspect seal then restart service'});vm.mock_web(r'log-two\.example',{'status':200,'body':'independent log: isolate equipment, inspect seal, restart service'});vm.mock_llm(r'.*SequenceWitness.*','{"verdict":"'+v+'"}')
def fresh(vm,deploy,alice,v='IN_ORDER'):
 vm.sender=alice;x=deploy(CONTRACT);x.register_sequence('sw-1',STEPS,A,B);seed(vm,v);return x
def test_ordered_sequence_seals(direct_vm,direct_deploy,direct_alice):
 x=fresh(direct_vm,direct_deploy,direct_alice);x.verify_sequence('SW-1');assert x.get_sequence('SW-1')['state']=='SEALED'
def test_non_ordered_sequence_correctable_once(direct_vm,direct_deploy,direct_alice):
 x=fresh(direct_vm,direct_deploy,direct_alice,'OUT_OF_ORDER');x.verify_sequence('SW-1');assert x.get_sequence('SW-1')['state']=='CORRECTABLE';x.replace_source('SW-1',1,'https://log-three.example/c');assert x.get_sequence('SW-1')['state']=='OPEN'
def test_duplicate_source_and_forged_digest_rejected(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT)
 with direct_vm.expect_revert('complete independent sequence required'):x.register_sequence('X',STEPS,A,A)
 x.register_sequence('sw-1',STEPS,A,B);seed(direct_vm);r=x.records['SW-1'];out=x._verify(r);assert direct_vm.run_validator(leader_result=out) is True;bad=dict(out);bad['digests']=list(reversed(out['digests']));assert direct_vm.run_validator(leader_result=bad) is False
