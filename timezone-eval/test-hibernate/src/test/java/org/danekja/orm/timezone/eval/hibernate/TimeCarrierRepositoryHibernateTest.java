package org.danekja.orm.timezone.eval.hibernate;

import org.danekja.orm.timezone.eval.TimeCarrierRepositoryTest;
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

/**
 * Date: 29.7.15
 *
 * @author Jakub Danek
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = HibernateAppConfig.class)
public class TimeCarrierRepositoryHibernateTest extends TimeCarrierRepositoryTest {
}
