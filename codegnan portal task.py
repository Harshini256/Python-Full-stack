codegnan_portal = {}
codegnan_portal['courses'] = ['PFS','DA','JFS','AI']
codegnan_portal['students_PFS'] = ['harshini','sarath','yaswanth','deelip']
codegnan_portal['students_DA'] = ['bhaagi','sneha','sharon','vaishu']
codegnan_portal['students_JFS'] = ['indhu','rekha','sakshi']
codegnan_portal.update({'Name of the institution':('CODEGNAN'),
                'Branches of Institute': ('vizag','hyderabad','vijayawada'),
                'subjects':('python','aptitude','softkills','Mysql','html','css','javascript'),
                'exams':('daily exams','weekly exams','Grand test'),
                'mock interviews':('evry saturday and sunday'),
                'projects': ('Atm pin change'),
                'couse completion months' : ('4 months'),
                'total_batches in PFS' : [1,2,3,4,5,6],
                'total_batches in DA' : [1,2,3,4,5,6,7],
                'total_batches in JFS' : [1,2,3,4],
                'class timings' : ('9 am to 5 pm'),
                'daily exam timings' : ('7 pm to 11 pm')
                })
codegnan_portal['students_PFS'].extend(['kusuma', 'thanusree'])
codegnan_portal['courses'].extend(['Testing course'])

print(len(codegnan_portal))
print(codegnan_portal)

                
                
