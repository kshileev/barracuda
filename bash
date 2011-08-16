Barracuda=/root/barracuda
Venv=/root/BaEnv
Port=`grep  -oE "[0-9]+" $Barracuda/nginx`

function ba_create_venv () 
{ 
    echo +++++++++++++++++++++PIP+++++++++++++++++++++++++++;
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++;
    [ -d $Venv ] || virtualenv --no-site-packages $Venv;
    $Venv/bin/pip install -r $Barracuda/pip-requirements-deploy.txt;
    return $?
}
function ba_get_from_github () 
{ 
    echo +++++++++++++++++++++GIT+++++++++++++++++++++++++++;
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++;
    [ -d $Barracuda ] && ( cd $Barracuda;
    git pull ) || git clone git://github.com/kshileev/barracuda.git $Barracuda;
    return $?
}
function ba_init () 
{ 
    ba_get_from_github || return;
    ba_create_venv || return;
    . $Venv/bin/activate;
    ba_manage syncdb
}
function ba_manage () 
{ 
    [ -f $Barracuda/manage.py ] || ( echo no barracude- run binit!;
    return );
    [ -f $Venv/bin/python ] || ( echo no BarEnv- run binit!;
    return );
    $Venv/bin/python $Barracuda/manage.py $@
}
function ba_reset () 
{ 
    rm -i -rf $Barracuda $Venv;
    ba_init
}
function ba_run () 
{ 
    ba_manage runfcgi host=127.0.0.1 port=$Port daemonize=true
}
function ba_debug () 
{ 
    ba_manage runfcgi host=127.0.0.1 port=$Port daemonize=false
}
