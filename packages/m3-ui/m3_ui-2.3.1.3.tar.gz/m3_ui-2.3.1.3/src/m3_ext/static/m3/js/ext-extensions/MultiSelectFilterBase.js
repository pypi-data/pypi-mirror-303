Ext.ns('Ext.m3');

/**
 * @class Ext.ux.form.MultiSelectFilterBase
 * @extends Ext.m3.MultiSelectField
 *
 * Базовый класс колоночных фильтров с множественным выбором.
 * Самостоятельно не инстанцируется
 */
Ext.m3.MultiSelectFilterBase = Ext.extend(Ext.m3.MultiSelectField, {
    /**
     * Id опции Выделить все
     */
    optAllId: -5,

    /**
     * Если снято выделение со всех записей то параметр не отправляется
     */
    skipEmptyValue: true
});

Ext.reg('m3-multiselect-filter-base', Ext.m3.MultiSelectFilterBase);