package org.danekja.orm.timezone.eval;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 * Date: 29.7.15
 *
 * @author Jakub Danek
 */
@Entity
public class TimeCarrier {

    private Long id;
    private Date date;

    public TimeCarrier() {
    }

    public TimeCarrier(Date date) {
        this.date = date;
    }

    @Id
    @GeneratedValue
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Temporal(TemporalType.TIMESTAMP)
    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof TimeCarrier)) return false;

        TimeCarrier that = (TimeCarrier) o;

        return !(date != null ? !date.equals(that.date) : that.date != null);

    }

    @Override
    public int hashCode() {
        return date != null ? date.hashCode() : 0;
    }
}
