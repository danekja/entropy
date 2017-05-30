package org.danekja.orm.timezone.eval.hibernate;

import org.danekja.orm.timezone.eval.AppConfig;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.jpa.JpaVendorAdapter;
import org.springframework.orm.jpa.vendor.Database;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;

/**
 * Date: 29.7.15
 *
 * @author Jakub Danek
 */
@Configuration
public class HibernateAppConfig extends AppConfig {

    @Override
    public JpaVendorAdapter jpaVendorAdapter() {
        HibernateJpaVendorAdapter jpaVendorAdapter = new HibernateJpaVendorAdapter();
        jpaVendorAdapter.setDatabase(Database.H2);
        jpaVendorAdapter.setGenerateDdl(true);
        return jpaVendorAdapter;
    }
}
