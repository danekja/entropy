package org.danekja.orm.timezone.eval;

import static org.junit.Assert.*;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

/**
 * Date: 29.7.15
 *
 * @author Jakub Danek
 */
public abstract class TimeCarrierRepositoryTest {

    @Autowired
    private TimeCarrierRepository repository;

    @Test
    public void testTimezoneShift() throws Exception {
        TimeZone.setDefault(TimeZone.getTimeZone("Europe/Helsinki"));
        DateFormat formatter= new SimpleDateFormat("MM/dd/yyyy HH:mm:ss Z");
        formatter.setTimeZone(TimeZone.getTimeZone("Europe/London"));

        TimeCarrier c = new TimeCarrier(new Date());
        c = repository.save(c);
        String correctVal = formatter.format(c.getDate());


        TimeCarrier l = repository.findOne(c.getId());
        String dbVal = formatter.format(l.getDate());
        assertEquals(correctVal, dbVal);

        TimeZone.setDefault(TimeZone.getTimeZone("Europe/Prague"));
        l = repository.findOne(c.getId());
        dbVal = formatter.format(l.getDate());

        assertNotEquals(correctVal, dbVal);
    }

    private boolean equal(long nb1, long nb2) {
        long diff = nb1 - nb2;
        return Math.abs(diff) < 1000;
    }
}
