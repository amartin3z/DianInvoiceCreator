import os
from collections import namedtuple
import subprocess

disk_ntuple = namedtuple('partition',  'device mountpoint fstype')
usage_ntuple = namedtuple('usage',  'total used free percent')
PROC_FILESYSTEMS = "/proc/filesystems"
ETC_MTAB = '/etc/mtab'


def get_disk_partitions():
    """Return all mountd partitions as a nameduple.
    """
    phydevs = []
    retlist = []

    assert os.path.exists(PROC_FILESYSTEMS)
    assert os.path.exists(ETC_MTAB)

    with open(PROC_FILESYSTEMS, 'r') as proc_fp:
        phydevs = [
            line.strip()
            for line in proc_fp
            if not line.startswith("nodev")
        ]

    with open(ETC_MTAB, 'r') as mtab_fp:
        for line in mtab_fp:
            if line.startswith('none'):
                continue

            device, mountpoint, fstype = line.split()[:3]

            if fstype not in phydevs:
                continue

            retlist.append(disk_ntuple(device, mountpoint, fstype))
    return retlist


def disk_usage(path):
    """Return disk usage associated with path."""
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    try:
        percent = (float(used) / total) * 100
    except ZeroDivisionError:
        percent = 0
    # NB: the percentage is -5% than what shown by df due to
    # reserved blocks that we are currently not considering:
    # http://goo.gl/sWGbH
    return usage_ntuple(total, used, free, round(percent, 1))


def du(path):

    subtotals = {}
    path = '/var/herbalife'
    subpaths = ['download', 'providers', 'satfiles']

    total = subprocess.check_output(['du','-s', path]).split()[0]
    subtotals['total'] = total
    for subpath in subpaths:
        subtotal = subprocess.check_output(['du','-s', os.path.join(path, subpath)]).split()[0]
        subtotals[subpath] = subtotal

    for subtotal in subtotals:
        if subtotal == 'total':
            continue
        #value = round(float(subtotals[subtotal])/float(total) * 100, 1)
        value = float(subtotals[subtotal])/float(total) * 100
        print '{} => {}%'.format(subtotal, value)
    print 'Total => {}'.format(total)
    print subtotals

if __name__ == '__main__':
    for part in get_disk_partitions():
        print part
        print "    %s\n" % str(disk_usage(part.mountpoint))